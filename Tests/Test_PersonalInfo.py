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