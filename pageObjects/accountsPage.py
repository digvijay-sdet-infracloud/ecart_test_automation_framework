from pageObjects.basePage import BasePage


class AccountsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.accounts_menu_items = page.locator("nav#menu ul")
        self.ecart_total_items = page.locator("#cart-total")


    def add_mac_desktop_to_cart(self):

      try:
        if self.page.get_by_role('link', name='Desktops').is_visible():
            self.page.get_by_role('link', name='Desktops').click()
            self.page.get_by_role('link', name='Mac (1)').click()
            self.page.get_by_role('button', name='Add to Cart').click()
      except Exception as e:
            print(f"An error occurred while adding Mac desktop to cart: {e}")
    

    def verify_item_is_added_to_cart(self):
        
        if self.ecart_total_items.is_visible():
           if self.ecart_total_items.get_by_text("Your shopping cart is empty!").is_visible():
               print("The cart is empty.")
           else:
               self.add_mac_desktop_to_cart()
        else:
            print("Already items present in the cart.")