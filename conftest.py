import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()