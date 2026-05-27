from playwright.sync_api import Page, Locator, expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInformationPage, CheckoutOverviewPage, CheckoutCompletePage
import allure
from faker import Faker

@allure.feature("Оплата")
@allure.title("Е2Е оплата товара")
def test_full_checkout_flow(page: Page, inventory_page: InventoryPage):
    first_item: Locator = inventory_page.inventory_items.first
    first_item_name: str = first_item.get_by_test_id("inventory-item-name").inner_text()
    first_item_price: str = first_item.get_by_test_id("inventory-item-price").inner_text()
    
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
    
    checkout_info_page = CheckoutInformationPage(page)
    fake = Faker('ru_RU')
    random_name = fake.first_name()
    random_lastname = fake.last_name()
    random_postal = fake.postcode()
    
    checkout_info_page.fill_personal_info(random_name, random_lastname, random_postal)
    
    checkout_info_page.to_overview()
    
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_item = checkout_overview_page.inventory_item.first
    overview_itemname = checkout_overview_item.get_by_test_id("inventory-item-name")
    overview_price = checkout_overview_item.get_by_test_id("inventory-item-price")
    overview_total_price = checkout_overview_page.total_price
    final_price = checkout_overview_page.get_final_cost()
    
    expect(overview_itemname).to_have_text(first_item_name)
    expect(overview_price).to_have_text(first_item_price)
    expect(overview_total_price).to_have_text("Total: $" + final_price)
    
    checkout_overview_page.finish()
    
    checkout_complete_page = CheckoutCompletePage(page)
    expect(checkout_complete_page.complete_container).to_be_visible()
    
    checkout_complete_page.back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    