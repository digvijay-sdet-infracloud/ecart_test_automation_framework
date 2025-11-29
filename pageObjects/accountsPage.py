from pageObjects.basePage import BasePage


class AccountsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.accounts_menu_items = page.locator("nav#menu ul")
        