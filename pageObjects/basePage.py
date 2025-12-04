class BasePage:

    def __init__(self, page):
        self.page = page

    
    def locator_get_by_role(self, role, name, exact=True):
        return self.page.get_by_role(role, name=name, exact=exact)
    
    def locator_get_by_text(self, text, exact=True):
        return self.page.get_by_text(text, exact=exact)

    def locator_get_by_placeholder(self, placeholder, exact=True):
        return self.page.get_by_placeholder(placeholder, exact=exact)

    def locator_get_by_css(self, selector):
        return self.page.locator(selector)

    def locator_get_by_id(self, id):
        return self.page.locator(f"#{id}")

    def locator_get_by_name(self, name):
        return self.page.locator(f"[name='{name}']")
    
   
    def login_orange_hrm_app(self, username, password):
        username_locator = self.locator_get_by_role('textbox', name='E-Mail Address')
        password_locator = self.locator_get_by_role('textbox', name='Password')
        login_button_locator = self.locator_get_by_role('button', name='Login')
        self.locator_get_by_role("link", name="My Account").first.click()
        self.locator_get_by_role("link", name="Login").first.click()
        username_locator.fill(username)
        password_locator.fill(password)
        login_button_locator.click()

    

    def do_logout(self):
        self.page.get_by_role("link", name="My Account").first.click()
        self.page.get_by_role("link", name="Logout").first.click()