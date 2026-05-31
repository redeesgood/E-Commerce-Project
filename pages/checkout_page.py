from playwright.sync_api import Page, Locator
from decimal import Decimal, ROUND_HALF_UP
import allure


class CheckoutInformationPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.first_name: Locator = page.get_by_test_id("firstName")
        self.last_name: Locator = page.get_by_test_id("lastName")
        self.postal_code: Locator = page.get_by_test_id("postalCode")

        self.continue_btn: Locator = page.get_by_test_id("continue")

        self.cancel_btn: Locator = page.get_by_test_id("cancel")

    @allure.step('Нажимаем "Продолдижть"')
    def to_overview(self) -> None:
        self.continue_btn.click()

    @allure.step('Нажимаем "Отмена"')
    def cancel(self) -> None:
        self.cancel_btn.click()

    @allure.step("Заполняем данные пользователя")
    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)


class CheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.finish_btn: Locator = page.get_by_test_id("finish")
        self.inventory_item: Locator = page.get_by_test_id("inventory-item")
        self.total_price: Locator = page.get_by_test_id("total-label")
        self.item_price: Locator = page.get_by_test_id("subtotal-label")
        self.tax_price: Locator = page.get_by_test_id("tax-label")

    @allure.step('Нажимаем "Завершить"')
    def finish(self) -> None:
        self.finish_btn.click()

    @allure.step("Складываем стоимость товаров и налог")
    def get_final_cost(self) -> str:
        raw_price = self.item_price.inner_text()
        clean_price = raw_price.replace("Item total: $", "")

        item_price = Decimal(clean_price)

        tax_rate = Decimal("0.08")
        tax_cost = (item_price * tax_rate).quantize(
            Decimal("0.00"), rounding=ROUND_HALF_UP
        )

        final_cost = item_price + tax_cost

        return f"{final_cost:.2f}"


class CheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.back_home_btn: Locator = page.get_by_test_id("back-to-products")

        self.complete_container: Locator = page.get_by_test_id(
            "checkout-complete-container"
        )

    @allure.step('Нажимаем "Вернуться Домой"')
    def back_home(self) -> None:
        self.back_home_btn.click()
