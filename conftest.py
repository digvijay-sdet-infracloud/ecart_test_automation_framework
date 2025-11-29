import json
import os
import allure
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):

    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against"
    )
    parser.addoption(
        "--username", action="store", help="Username for authentication"
    )
    parser.addoption(
        "--password", action="store", help="Password for authentication"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")

    # create full path to JSON file
    path = os.path.join("config", f"{env}.json")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    # LOAD JSON and return dict
    with open(path, "r") as f:
        data = json.load(f)

    return data


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def credentials(request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    return {"username": username, "password": password}


@pytest.fixture(scope="function", autouse=True)
def before_each_test(page, config, credentials):
    """
    Automatically runs before each test:
    - Navigates to environment base URL
    - Logs in if username + password are provided
    """

    # 1. Navigate to base URL from config JSON
    base_url = config["base_url"]
    page.goto(base_url)

    # 2. Auto-login if credentials provided
    if credentials["username"] and credentials["password"]:
        
        username_locator = page.get_by_role('textbox', name='E-Mail Address')
        password_locator = page.get_by_role('textbox', name='Password')
        login_button_locator = page.get_by_role('button', name='Login')

        username_locator.fill(credentials["username"])
        password_locator.fill(credentials["password"])
        login_button_locator.click()
        page.wait_for_load_state("networkidle")

    return page

@pytest.fixture(autouse=True)
def after_each_test(page):

    yield

    # Logout after each test
    page.get_by_role("link", name="My Account").first.click()
    page.get_by_role("link", name="Logout").first.click()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # Screenshot
            allure.attach(
                page.screenshot(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

            # HTML Source
            allure.attach(
                page.content(),
                name="page_source",
                attachment_type=allure.attachment_type.HTML
            )