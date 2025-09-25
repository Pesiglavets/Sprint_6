import pytest
from selenium import webdriver
"""from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager"""

    # Настройка Chrome драйвера
"""@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()"""

    # Настройка Firefox драйвера
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()