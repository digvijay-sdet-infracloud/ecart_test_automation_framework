from pageObjects.basePage import BasePage
import pytest
from playwright.sync_api import expect

from pageObjects.accountsPage import AccountsPage


def test_ecart_account_page_validations(page):
     expect(page).to_have_title("My Account")


def test_ecart_account_menu_items(page):

     account_page = AccountsPage(page)
     expect(account_page.accounts_menu_items).to_have_count(8)

def test_verify_ecart_account_is_empty(page):
     
     account_page = AccountsPage(page)
     expect(account_page.ecart_total_items).to_be_visible()
     expect(account_page.ecart_total_items).to_have_text("0 item(s) - $0.00")

@pytest.mark.smoke("smoke")
def test_add_mac_desktop_to_cart(page):

     account_page = AccountsPage(page)
     base_page  = BasePage(page)
     account_page.verify_item_is_added_to_cart()
     expect(account_page.ecart_total_items).to_have_text("1 item(s) - $122.00")
     account_page.ecart_total_items.click()
     expect(page.get_by_role("link", name="iMac").last).to_be_visible()
