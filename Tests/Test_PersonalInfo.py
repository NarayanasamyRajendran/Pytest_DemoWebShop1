import pytest
from Pages.PersonalInfo_page import PersonalInformation
from Utility import utility_file

@pytest.mark.usefixtures("test_setup_and_setdown")
class Test_PersonalInfo:
    def test_login_form(self):
        information = PersonalInformation(self.driver, utility_file)
        information.fill_login_form()

    def test_cust_form(self):
        information1 = PersonalInformation(self.driver, utility_file)
        information1.fill_login_form()
        information1.click_gender()
        information1.enter_firstname()
        information1.enter_lastname()
        information1.enter_emailname()
        information1.click_save_account()

    def test_customer_address(self):
        information2 = PersonalInformation(self.driver, utility_file)
        information2.fill_login_form()
        information2.click_cust_address()
        information2.click_addNew()
        information2.enter_addr_firstname()
        information2.enter_addr_lastname()
        information2.enter_addr_email()
        information2.click_country()
        information2.select_country()
        information2.enter_city()
        information2.enter_address1()
        information2.enter_zipCode()
        information2.enter_phoneNumber()
        information2.save_address()
        #information2.assert_address_saved()

    def test_customer_orders(self):
        information3 = PersonalInformation(self.driver, utility_file)
        information3.fill_login_form()
        information3.click_orders_button()
        information3.assert_NoOrders()

    def test_customer_download(self):
        information4 = PersonalInformation(self.driver, utility_file)
        information4.fill_login_form()
        information4.click_download()
        information4.assert_NoDownload()

    def test_customer_sub(self):
        information5 = PersonalInformation(self.driver, utility_file)
        information5.fill_login_form()
        information5.click_sub()
        information5.assert_NoSub()

    def test_customer_reward(self):
        information6 = PersonalInformation(self.driver, utility_file)
        information6.fill_login_form()
        information6.click_reward()
        information6.assert_Noreward()

    def test_customer_changepass(self):
        information7 = PersonalInformation(self.driver, utility_file)
        information7.fill_login_form()
        information7.click_changepass()
        information7.enter_old_pass()
        information7.enter_new_pass()
        information7.enter_con_new_pass()
        information7.click_submit_password()
        information7.assert_password_change()
