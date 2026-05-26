from playwright.sync_api import Page, Locator
import allure

class CartPage:
    def __init__ (self, page: Page) -> None:
        self.page = page
        
        self.continue_shopping_btn: Locator = page.get_by_test_id("continue-shopping")
        
        self.checkout_btn: Locator = page.get_by_test_id("checkout")
        
        self.cart_badge: Locator = page.get_by_test_id("shopping-cart-badge")


    @allure.step('Нажимаем "Отмена"')
    def to_continue_shopping(self) -> None:
        self.continue_shopping_btn.click()
    
    @allure.step('Нажимаем "Продолжить"')
    def to_checkout(self) -> None:
        self.checkout_btn.click()
        
    
    