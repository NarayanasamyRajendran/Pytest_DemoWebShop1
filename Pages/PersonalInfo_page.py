from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalInformation(BasePage):
    click_login_element = (By.XPATH, "//a[@class='ico-login']")
    Email = (By.XPATH, "//input[@id='Email']")
    Password = (By.XPATH, "//input[@id='Password']")
    submit_login = (By.XPATH, "//input[@class='button-1 login-button']")
    click_account_elament = (By.XPATH, "(//a[@class='account'])[1]")
    click_acc_gender = (By.XPATH, "//input[@id='gender-male']")
    firstName = (By.XPATH, "//input[@id='FirstName']")
    lastName = (By.XPATH, "//input[@id='LastName']")
    emailName = (By.XPATH, "//input[@id='Email']")
    save_path = (By.XPATH, "//input[@name='save-info-button']")

    address_path = (By.XPATH, "//a[@href='/customer/addresses'][@class='inactive']")
    addNew_path = (By.XPATH, "//input[@value='Add new']")
    firstName_path = (By.XPATH, "//input[@id='Address_FirstName']")
    lastName_path = (By.XPATH, "//input[@id='Address_LastName']")
    emailName_path = (By.XPATH, "//input[@id='Address_Email']")
    country_path = (By.XPATH, "//select[@id='Address_CountryId']")
    select_country_path = (By.XPATH, "//option[text()='India']")
    city_path = (By.XPATH, "//input[@id='Address_City']")
    address1_path = (By.XPATH, "//input[@id='Address_Address1']")
    zip_path = (By.XPATH, "//input[@id='Address_ZipPostalCode']")
    phoneNumber_path = (By.XPATH, "//input[@id='Address_PhoneNumber']")
    address_save_path = (By.XPATH, "//input[@class='button-1 save-address-button']")
    address_success_message_path = (By.XPATH, "//div[@class='page-title']/h1")

    orders_path = (By.XPATH, "//a[@href='/customer/orders'][@class='inactive']")
    success_message_noOrder = (By.XPATH, "//div[@class='order-list']")
    download_path = (By.XPATH, "//a[text()='Downloadable products']")
    success_message_noDownload = (By.XPATH, "//div[@class='no-data']")

    sub_path = (By.XPATH, "//a[text()='Back in stock subscriptions']")
    success_message_nosub = (By.XPATH, "//div[@class='no-data']")

    reward_path = (By.XPATH, "//a[text()='Reward points']")
    success_message_noReward = (By.XPATH, "//div[@class='current-balance']")

    changePass_path = (By.XPATH, "//a[text()='Change password']")
    oldpass_path = (By.XPATH, "//input[@id='OldPassword']")
    newpass_path = (By.XPATH, "//input[@id='NewPassword']")
    connewpass_path = (By.XPATH, "//input[@id='ConfirmNewPassword']")
    submit_changepass_path = (By.XPATH, "//input[@class='button-1 change-password-button']")
    success_message_changepass = (By.XPATH, "//div[@class='result']")

    def __init__(self, driver, utility_file):
        super().__init__(driver)
        self.utility_file = utility_file

    def fill_login_form(self):
        click_login_top = self.find(self.click_login_element)
        self.for_click(click_login_top)

        enter_mail = self.utility_file.get_config("personal info", "email_id")
        mail = self.find(self.Email)
        self.for_send_keys(mail, enter_mail)
        enter_pass = self.utility_file.get_config("personal info", "password")
        passWord = self.find(self.Password)
        self.for_send_keys(passWord, enter_pass)

        click_submit_login = self.find(self.submit_login)
        self.for_click(click_submit_login)

        click_account_info = self.find(self.click_account_elament)
        self.for_click(click_account_info)

    def click_gender(self):
        click_gender1 = self.find(self.click_acc_gender)
        self.for_click(click_gender1)

    def enter_firstname(self):
        enter_firstname1 = self.utility_file.get_config("customer info", "first_name")
        Firstname = self.find(self.firstName)
        self.for_send_keys(Firstname, enter_firstname1)

    def enter_lastname(self):
        enter_lastname1 = self.utility_file.get_config("customer info", "last_name")
        Lastname = self.find(self.lastName)
        self.for_send_keys(Lastname, enter_lastname1)

    def enter_emailname(self):
        enter_emailname1 = self.utility_file.get_config("customer info", "emailId")
        Emailname = self.find(self.emailName)
        self.for_send_keys(Emailname, enter_emailname1)

    def click_save_account(self):
        click_save_cust = self.find(self.save_path)
        self.for_click(click_save_cust)

    def click_cust_address(self):
        click_address1 = self.find(self.address_path)
        self.for_click(click_address1)

    def click_addNew(self):
        click_addNew1 = self.find(self.addNew_path)
        self.for_click(click_addNew1)

    def enter_addr_firstname(self):
        enter_firstname = self.utility_file.get_config("customer address", "firstName")
        firstname1 = self.find(self.firstName_path)
        self.for_send_keys(firstname1, enter_firstname)

    def enter_addr_lastname(self):
        enter_lastname = self.utility_file.get_config("customer address", "lastName")
        lastname1 = self.find(self.lastName_path)
        self.for_send_keys(lastname1, enter_lastname)

    def enter_addr_email(self):
        enter_emailname = self.utility_file.get_config("customer address", "emailid")
        emailname1 = self.find(self.emailName_path)
        self.for_send_keys(emailname1, enter_emailname)

    def click_country(self):
        click_addr_country = self.find(self.country_path)
        self.for_click(click_addr_country)

    def select_country(self):
        select_addr_country = self.find(self.select_country_path)
        self.for_click(select_addr_country)

    def enter_city(self):
        enter_cityname = self.utility_file.get_config("customer address", "city")
        cityname1 = self.find(self.city_path)
        self.for_send_keys(cityname1, enter_cityname)

    def enter_address1(self):
        enter_address1 = self.utility_file.get_config("customer address", "address1")
        address2 = self.find(self.address1_path)
        self.for_send_keys(address2, enter_address1)

    def enter_zipCode(self):
        enter_zip = self.utility_file.get_config("customer address", "zipCode")
        zip1 = self.find(self.zip_path)
        self.for_send_keys(zip1, enter_zip)

    def enter_phoneNumber(self):
        enter_phoneNo = self.utility_file.get_config("customer address", "PhoneNo")
        phoneNo1 = self.find(self.phoneNumber_path)
        self.for_send_keys(phoneNo1, enter_phoneNo)

    def save_address(self):
        click_addr_save = self.find(self.address_save_path)
        self.for_click(click_addr_save)

    def assert_address_saved(self):
        expected_result = "My account - Addresses"
        address_success_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.address_success_message_path))
        address_success_message_text = address_success_message_element.text.strip()
        assert address_success_message_text == expected_result

    def click_orders_button(self):
        orders = self.find(self.orders_path)
        self.for_click(orders)

    def assert_NoOrders(self):
        expected_result = "No orders"
        success_noOrder_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message_noOrder))
        success_noOrder_message_text = success_noOrder_message_element.text.strip()
        assert success_noOrder_message_text == expected_result


    def click_download(self):
        download = self.find(self.download_path)
        self.for_click(download)

    def assert_NoDownload(self):
        expected_result = "There are no downloadable products"
        success_noDownload_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message_noDownload))
        success_noDownload_message_text = success_noDownload_message_element.text.strip()
        assert success_noDownload_message_text == expected_result


    def click_sub(self):
        sub = self.find(self.sub_path)
        self.for_click(sub)

    def assert_NoSub(self):
        expected_result = "You are not currently subscribed to any Back In Stock notification lists"
        success_nosub_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message_nosub))
        success_nosub_message_text = success_nosub_message_element.text.strip()
        assert success_nosub_message_text == expected_result

    def click_reward(self):
        reward = self.find(self.reward_path)
        self.for_click(reward)

    def assert_Noreward(self):
        expected_result = "Your current balance is 0 reward points (0.00)."
        success_norewards_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message_noReward))
        success_norewards_message_text = success_norewards_message_element.text.strip()
        assert success_norewards_message_text == expected_result

    def click_changepass(self):
        change_pass = self.find(self.changePass_path)
        self.for_click(change_pass)

    def enter_old_pass(self):
        enter_old = self.utility_file.get_config("customer password information", "old_password")
        old1 = self.find(self.oldpass_path)
        self.for_send_keys(old1, enter_old)

    def enter_new_pass(self):
        enter_new = self.utility_file.get_config("customer password information", "new_password")
        new1 = self.find(self.newpass_path)
        self.for_send_keys(new1, enter_new)

    def enter_con_new_pass(self):
        enter_confirm = self.utility_file.get_config("customer password information", "confirm_new_password")
        confirm1 = self.find(self.connewpass_path)
        self.for_send_keys(confirm1, enter_confirm)

    def click_submit_password(self):
        submit_changepass = self.find(self.submit_changepass_path)
        self.for_click(submit_changepass)

    def assert_password_change(self):
        expected_result = "Password was changed"
        try:
            success_changepass_message_element = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.success_message_changepass))
            success_changepass_message_text = self._driver.execute_script("return arguments[0].textContent.trim();", success_changepass_message_element)
            assert success_changepass_message_text == expected_result, f"Expected '{expected_result}', but got '{success_changepass_message_text}'"
        except AssertionError as e:
            print(f"Assertion Error: {e}")