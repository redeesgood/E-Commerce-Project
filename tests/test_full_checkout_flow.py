from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInformationPage, CheckoutOverviewPage, CheckoutCompletePage
import allure
from faker import Faker

@allure.feature("Оплата")
@allure.title("Е2Е оплата товара")
def test_full_checkout_flow(page: Page, inventory_page: InventoryPage):
    first_item = inventory_page.inventory_items.first
    first_item.locator("button.btn_inventory").click()
    
    inventory_page.cart_btn.click()
    
    cart_page = CartPage(page)
    cart_page.to_checkout()
    
    checkout_info_page = CheckoutInformationPage(page)
    fake = Faker('ru_RU')
    random_name = fake.first_name()
    random_lastname = fake.last_name()
    random_postal = fake.postcode()
    
    checkout_info_page.fill_personal_info(random_name, random_lastname, random_postal)
    
    checkout_info_page.to_overview()
    
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.finish()
    
    checkout_complete_page = CheckoutCompletePage(page)
    expect(checkout_complete_page.complete_container).to_be_visible()
    
    checkout_complete_page.back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    