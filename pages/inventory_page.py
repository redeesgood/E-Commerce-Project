from playwright.sync_api import Page, Locator
import allure


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.sort_list: Locator = page.get_by_test_id("product-sort-container")

        self.inventory_items: Locator = page.get_by_test_id("inventory-item")

        self.cart_badge: Locator = page.get_by_test_id("shopping-cart-badge")

        self.cart_btn: Locator = page.get_by_test_id("shopping-cart-link")

        self.burger_btn: Locator = page.locator("#react-burger-menu-btn")

        self.logout_btn: Locator = page.get_by_test_id("logout-sidebar-link")

    @allure.step("Выбираем тип сортировки: {sort_option}")
    def sort_by(self, sort_option: str) -> None:
        self.sort_list.select_option(value=sort_option)

    @allure.step("Получаем все цены товаров на странице")
    def get_all_prices(self) -> list[float]:
        prices = self.page.get_by_test_id("inventory-item-price").all_inner_texts()

        return [float(price.replace("$", "")) for price in prices]

    @allure.step("Получаем все названия товаров на странице")
    def get_all_names(self) -> list[str]:
        return self.page.get_by_test_id("inventory-item-name").all_inner_texts()

    @allure.step("Переходим в корзину")
    def to_cart(self) -> None:
        self.cart_btn.click()

    @allure.step("Открываем боковое окно и выходим из аккаунта")
    def logout(self) -> None:
        self.burger_btn.click()
        self.logout_btn.click()
