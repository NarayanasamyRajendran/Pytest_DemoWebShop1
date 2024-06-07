import pytest
from selenium import webdriver
from Utility import utility_file

@pytest.fixture()
def test_setup_and_setdown(request):
    browser = utility_file.get_config("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    url = utility_file.get_config("basic info", "url")
    driver.get(url)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
