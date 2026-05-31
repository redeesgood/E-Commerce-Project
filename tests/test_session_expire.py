from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import expect, Page
import allure


@allure.feature("Сессия")
@allure.title("Истечение срока сессии")
def test_session_expiration(
    page: Page, inventory_page: InventoryPage, login_page: LoginPage
):
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.context.clear_cookies()
    page.reload()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.error_text).to_be_visible()
