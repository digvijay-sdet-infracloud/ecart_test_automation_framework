
from playwright.sync_api import expect

from pageObjects.accountsPage import AccountsPage

def test_accounts_page_title(page):
    expect(page).to_have_title("My Account")



def test_verify_menu_items_accounts(page):
    accounts_page = AccountsPage(page)
    expect(accounts_page.accounts_menu_items).to_have_count(8)
    

