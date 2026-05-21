import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.title("Успешный вход со стандартными данными")
def test_successful_login(page: Page, login_page: LoginPage):
    login_page.login("standard_user", "secret_sauce")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@allure.feature("Авторизация")
@allure.title("Неуспешный вход")
@pytest.mark.parametrize("username, password", [
    ("error", "sec"), # Неверные логин и пароль
    ("standard_user", "sec"), # Неверный пароль
    ("sec", "secret_sauce") # Неверный логин
])
def test_unseccessful_login (page: Page, login_page: LoginPage, username: str, password: str):
    login_page.login(username, password)
    expect(login_page.error_text).to_be_visible()
    
    login_page.close_error_message()
    expect(login_page.error_text).not_to_be_visible()