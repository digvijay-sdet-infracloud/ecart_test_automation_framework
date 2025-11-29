from playwright.sync_api import expect

from pageObjects.accountsPage import AccountsPage


def test_ecart_account_page_validations(page):
     expect(page).to_have_title("My Account")


def test_ecart_account_menu_items(page):

     account_page = AccountsPage(page)
     expect(account_page.accounts_menu_items).to_have_count(8)