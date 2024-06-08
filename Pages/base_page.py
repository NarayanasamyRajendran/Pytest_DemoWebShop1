from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 30)
        self._action = ActionChains(self._driver)

    def for_click(self, element):
        element.click()
    
    def find(self, locator):
        return self._driver.find_element(*locator)
    
    def for_send_keys(self,element,value):
        element.send_keys(value)
