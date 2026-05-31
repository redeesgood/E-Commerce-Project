from playwright.sync_api import Page, Locator, expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import (
    CheckoutInformationPage,
    CheckoutOverviewPage,
    CheckoutCompletePage,
)
import allure
from faker import Faker


@allure.feature("Оплата товара")
@allure.title("Е2Е оплата одного товара")
def test_full_checkout_flow_one_item(page: Page, inventory_page: InventoryPage):
    first_item: Locator = inventory_page.inventory_items.first
    first_item_name: str = first_item.get_by_test_id("inventory-item-name").inner_text()
    first_item_price: str = first_item.get_by_test_id(
        "inventory-item-price"
    ).inner_text()

    first_item.locator("button.btn_inventory").click()

    inventory_page.to_cart()
    cart_page = CartPage(page)
    cart_page_item: Locator = cart_page.inventory_item.first
    cart_itemname = cart_page_item.get_by_test_id("inventory-item-name")
    cart_price = cart_page_item.get_by_test_id("inventory-item-price")

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_itemname).to_have_text(first_item_name)
    expect(cart_price).to_have_text(first_item_price)

    cart_page.to_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    info_page = CheckoutInformationPage(page)

    fake = Faker("ru_RU")
    random_name = fake.first_name()
    random_lastname = fake.last_name()
    random_postal = fake.postcode()

    info_page.fill_personal_info(random_name, random_lastname, random_postal)

    info_page.to_overview()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    overview_page = CheckoutOverviewPage(page)
    overview_item = overview_page.inventory_item.first

    overview_itemname = overview_item.get_by_test_id("inventory-item-name")
    overview_price = overview_item.get_by_test_id("inventory-item-price")
    overview_total_price = overview_page.total_price

    final_price = overview_page.get_final_cost()

    expect(overview_itemname).to_have_text(first_item_name)
    expect(overview_price).to_have_text(first_item_price)
    expect(overview_total_price).to_have_text("Total: $" + final_price)

    overview_page.finish()

    complete_page = CheckoutCompletePage(page)
    expect(complete_page.complete_container).to_be_visible()

    complete_page.back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@allure.feature("Оплата товара")
@allure.title("Е2Е оплата нескольких товаров")
def test_full_checkout_flow_many_item(page: Page, inventory_page: InventoryPage):
    inventory_items = inventory_page.inventory_items.all()
    assert len(inventory_items) > 0, "Товары не найдены!"

    expected_items = []

    for item in inventory_items[:3]:
        inventory_name = item.get_by_test_id("inventory-item-name").inner_text()
        inventory_price = item.get_by_test_id("inventory-item-price").inner_text()
        expected_items.append({"name": inventory_name, "price": inventory_price})

        item.locator("button.btn_inventory").click()

    inventory_page.to_cart()

    cart_page = CartPage(page)
    cart_items = cart_page.inventory_item.all()
    expect(cart_page.inventory_item).to_have_count(len(expected_items))

    for expected, cart_item in zip(expected_items, cart_items):
        expect(cart_item.get_by_test_id("inventory-item-name")).to_have_text(
            expected["name"]
        )
        expect(cart_item.get_by_test_id("inventory-item-price")).to_have_text(
            expected["price"]
        )

    cart_page.to_checkout()

    info_page = CheckoutInformationPage(page)

    fake = Faker("ru_RU")
    random_name = fake.first_name()
    random_lastname = fake.last_name()
    random_postal = fake.postcode()

    info_page.fill_personal_info(random_name, random_lastname, random_postal)
    info_page.to_overview()

    overview_page = CheckoutOverviewPage(page)
    overview_items = overview_page.inventory_item.all()
    expect(overview_page.inventory_item).to_have_count(len(expected_items))

    for expected, overview_item in zip(expected_items, overview_items):
        expect(overview_item.get_by_test_id("inventory-item-name")).to_have_text(
            expected["name"]
        )
        expect(overview_item.get_by_test_id("inventory-item-price")).to_have_text(
            expected["price"]
        )

    final_price = overview_page.get_final_cost()
    expect(overview_page.total_price).to_have_text("Total: $" + final_price)

    overview_page.finish()

    complete_page = CheckoutCompletePage(page)
    expect(complete_page.complete_container).to_be_visible()

    complete_page.back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
