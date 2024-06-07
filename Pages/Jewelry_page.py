from selenium.webdriver.common.by import By
from Pages.BasePage import Basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Jewelry(Basepage):
    click_jewelrys = (By.XPATH, "(//a[@href='/jewelry'])[1]")
    click_jewelry_element1 = (By.XPATH, "//a[text()='Create Your Own Jewelry']")
    click_jewelry_element2 = (By.XPATH, "//a[text()='Black & White Diamond Heart']")
    click_addToCart_element = (By.XPATH, "//input[@id='add-to-cart-button-14']")
    success_message = (By.XPATH, "//p[@class='content']")
    click_wishlist_element = (By.XPATH, "//input[@id='add-to-wishlist-button-14']")
    #success_message1 = (By.XPATH, "//p[@class='content']")
    click_wishlist_on_top_element = (By.XPATH, "//span[text()='Wishlist']")
    wishlist_message = (By.XPATH, "//div[@class='wishlist-content']")
    click_sortBy_element = (By.XPATH, "//select[@id='products-orderby']")
    select_sortBy_element = (By.XPATH, "//option[text()='Name: A to Z']")
    click_display_element = (By.XPATH, "//select[@id='products-pagesize']")
    select_display_element = (By.XPATH, "//option[text()='8']")
    
    def __init__(self, driver):
        super().__init__(driver)

    def clickJewelry(self):
        click_jewelry_element = self.find(self.click_jewelrys)
        self.for_click(click_jewelry_element)

    def clickJewelry_first_product(self):
        click_jewelry_first_element = self.find(self.click_jewelry_element1)
        self.for_click(click_jewelry_first_element)

    def assert_visible_first_product(self):
        try:
            assert "Create Your Own Jewelry" in self._driver.title
        except AssertionError:
            print("Page does not match")
            raise

    def clickJewelry_second_product(self):
        click_jewelry_second_element = self.find(self.click_jewelry_element2)
        self.for_click(click_jewelry_second_element)

    def assert_visible_second_product(self):
        try:
            assert "Black & White Diamond Heart" in self._driver.title
        except AssertionError:
            print("Page does not match")
            raise

    def click_addToCart(self):
        click_addtocart = self.find(self.click_addToCart_element)
        self.for_click(click_addtocart)

    def assert_addToCart_Added(self):
        expected_result = "The product has been added to your shopping cart"
        success_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message))
        success_message_text = success_message_element.text.strip()
        assert success_message_text == expected_result

    def click_wishlist(self):
        click_wishlist = self.find(self.click_wishlist_element)
        self.for_click(click_wishlist)

    def assert_wishlist_Added(self):
        expected_result1 = "The product has been added to your wishlist"
        success_message_element1 = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message))
        success_message_text1 = success_message_element1.text.strip()
        assert success_message_text1 == expected_result1

    def click_wishlist_on_top(self):
        click_wishlist1 = self.find(self.click_wishlist_on_top_element)
        self.for_click(click_wishlist1)

    def assert_wishlist_empty(self):
        expected_result2 = "The wishlist is empty!"
        wishlist_message_text = self.find(self.wishlist_message).text.strip()
        assert wishlist_message_text == expected_result2

    def click_sortBy(self):
        click_sortby = self.find(self.click_sortBy_element)
        self.for_click(click_sortby)

    def select_sortBy(self):
        select_sortby = self.find(self.select_sortBy_element)
        self.for_click(select_sortby)

    def click_display(self):
        click_Display = self.find(self.click_display_element)
        self.for_click(click_Display)

    def select_display(self):
        select_Display = self.find(self.select_display_element)
        self.for_click(select_Display)