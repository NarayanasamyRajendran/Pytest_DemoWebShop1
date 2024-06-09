import pytest
from Pages.Jewelry_page import Jewelry

@pytest.mark.usefixtures("test_setup_and_setdown")
class Test_Jewelry:
    def test_jewelry_products(self):
        product = Jewelry(self.driver)
        product.clickJewelry()
        product.clickJewelry_first_product()
        product.assert_visible_first_product()

    def test_jewelry_addToCart(self):
        product1 = Jewelry(self.driver)
        product1.clickJewelry()
        product1.clickJewelry_second_product()
        product1.assert_visible_second_product()
        product1.click_addToCart()

    def test_jewelry_assertCart(self):
        product2 = Jewelry(self.driver)
        product2.clickJewelry()
        product2.clickJewelry_second_product()
        product2.assert_visible_second_product()
        product2.click_addToCart()
        product2.assert_addToCart_Added()

    def test_jewelry_empty_wishlist(self):
        product4 = Jewelry(self.driver)
        product4.clickJewelry()
        product4.clickJewelry_second_product()
        product4.assert_visible_second_product()
        product4.click_wishlist_on_top()
        product4.assert_wishlist_empty()

    def test_jewelry_assertwishlist(self):
        product3 = Jewelry(self.driver)
        product3.clickJewelry()
        product3.clickJewelry_second_product()
        product3.assert_visible_second_product()
        product3.click_wishlist()
        product3.assert_wishlist_Added()

    def test_jewelry_filter1(self):
        product5 = Jewelry(self.driver)
        product5.clickJewelry()
        product5.click_sortBy()
        product5.select_sortBy()
        product5.clickJewelry_second_product()
        product5.assert_visible_second_product()

    def test_jewelry_filter2(self):
        product6 = Jewelry(self.driver)
        product6.clickJewelry()
        product6.click_display()
        product6.select_display()
        product6.clickJewelry_second_product()
        product6.assert_visible_second_product()

    def test_jewelry_filter3(self):
        product7 = Jewelry(self.driver)
        product7.clickJewelry()
        product7.click_sortBy()
        product7.select_sortBy()
        product7.click_display()
        product7.select_display()
        product7.clickJewelry_second_product()
        product7.assert_visible_second_product()

    def test_jewelry_filterAll1(self):
        product7 = Jewelry(self.driver)
        product7.clickJewelry()
        product7.click_sortBy()
        product7.select_sortBy()
        product7.click_display()
        product7.select_display()
        product7.click_ViewAs()
        product7.select_ViewAs()
        product7.click_first_price()
        product7.assert_price_0_500()

    def test_jewelry_filterAll2(self):
        product7 = Jewelry(self.driver)
        product7.clickJewelry()
        product7.click_sortBy()
        product7.select_sortBy()
        product7.click_display()
        product7.select_display()
        product7.click_ViewAs()
        product7.select_ViewAs()
        product7.click_second_price()
        #product7.assert_price_500_700()