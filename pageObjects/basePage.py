class BasePage:

    def __init__(self, page):
        self.page = page


    def do_logout(self):
        self.page.get_by_role("link", name="My Account").click()
        self.page.get_by_role("link", name="Logout").click()