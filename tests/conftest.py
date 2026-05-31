import pytest
from playwright.sync_api import Page, Playwright
from typing import Generator
from db.db_core import DBHelper
from api.api_client import APIClient
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def db() -> Generator[DBHelper, None, None]:
    db_helper = DBHelper(":memory:")
    db_helper.create_tables()

    yield db_helper

    db_helper.close()


@pytest.fixture
def api() -> Generator[APIClient, None, None]:
    api_key = os.getenv("REQRES_API_KEY")
    assert api_key is not None, "API ключ не найден!"

    api = APIClient(api_key)

    yield api


@pytest.fixture()
def login_page(page: Page) -> Generator[LoginPage, None, None]:
    page.goto("https://www.saucedemo.com/")

    yield LoginPage(page)


@pytest.fixture()
def inventory_page(
    page: Page, login_page: LoginPage
) -> Generator[InventoryPage, None, None]:
    login_page.login("standard_user", "secret_sauce")

    yield InventoryPage(page)


# На странице SauceDemo атрибут называется data-test вместо data-testid
# Учим Playwright находить data-test и заменять на data-testid
@pytest.fixture(scope="session", autouse=True)
def set_test_id(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-test")
