import pytest
from selenium import webdriver
from Utility import read_config

@pytest.fixture()
def test_setup_and_setdown(request):
    browser = read_config.get_config("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    url = read_config.get_config("basic info", "url")
    driver.get(url)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
