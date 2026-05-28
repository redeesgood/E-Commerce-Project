from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import expect, Page
import allure

@allure.feature("Логаут")
@allure.title("Выход из аккаунта и переход в /inventory.html")
def test_logout_security(page: Page, inventory_page: InventoryPage, login_page: LoginPage):
    inventory_page.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")

    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.error_text).to_have_text("Epic sadface: You can only access '/inventory.html' when you are logged in.")    
    