from pages.inventory_page import InventoryPage
from playwright.sync_api import expect
import allure
import pytest


@allure.feature("Каталог товаров")
@allure.title("У каждого товара есть картинка, название, описание и цена")
def test_get_all_products_info(inventory_page: InventoryPage):
    items = inventory_page.inventory_items.all()
    assert len(items) > 0, "Товары не найдены"

    for item in items:
        expect(item.get_by_test_id("inventory-item-name")).to_be_visible()
        expect(item.get_by_test_id("inventory-item-desc")).to_be_visible()
        expect(item.get_by_test_id("inventory-item-price")).to_be_visible()
        expect(item.locator("img.inventory_item_img")).to_be_visible()


@allure.feature("Каталог товаров")
@allure.title("Проверка сортировки товаров по цене ASC и DESC")
@pytest.mark.parametrize("sort_value, reverse_sort", [("lohi", False), ("hilo", True)])
def test_prices_sort(
    inventory_page: InventoryPage, sort_value: str, reverse_sort: bool
):
    inventory_page.sort_by(sort_value)

    actual_prices = inventory_page.get_all_prices()
    expected_prices = sorted(actual_prices, reverse=reverse_sort)

    assert actual_prices == expected_prices, f"Сортировка {sort_value} не работает!"


@allure.feature("Каталог товаров")
@allure.title("Проверка сортировки по имени Z-A и A-Z")
def test_names_sort(inventory_page: InventoryPage):
    inventory_page.sort_by("za")

    actual_names = inventory_page.get_all_names()
    expected_names = sorted(actual_names, reverse=True)

    assert actual_names == expected_names, "Сортировка Z-A не работает!"

    inventory_page.sort_by("az")

    actual_names = inventory_page.get_all_names()
    expected_names = sorted(actual_names, reverse=False)

    assert actual_names == expected_names, "Сортировка A-Z не работает!"


@allure.feature("Каталог товаров")
@allure.title("Проверка работы счётчика")
def test_cart_badge(inventory_page: InventoryPage):
    items = inventory_page.inventory_items.all()
    expected_count = 0

    for item in items:
        btn = item.locator("button.btn_inventory")
        btn.click()

        expected_count += 1

        expect(inventory_page.cart_badge).to_have_text(str(expected_count))

    for item in items:
        btn = item.locator("button.btn_inventory")
        btn.click()

        expected_count -= 1

        if expected_count > 0:
            expect(inventory_page.cart_badge).to_have_text(str(expected_count))
        else:
            expect(inventory_page.cart_badge).not_to_be_visible()
