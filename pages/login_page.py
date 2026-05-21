from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__ (self, page: Page) -> None:
        self.page = page
        
        self.username: Locator = page.get_by_test_id("username")
        self.password: Locator = page.get_by_test_id("password")
        self.login_btn: Locator = page.get_by_test_id("login-button")

        self.error_text = page.get_by_test_id("error")
        self.error_btn = page.get_by_test_id("error-button")
        
    def login(self, username: str, password: str) -> None:
        self.username.fill(f"{username}")
        self.password.fill(f"{password}")
        self.login_btn.click()
        
    def close_error_message(self):
        self.error_btn.click()
        
    
    
        
    
    
        