import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument("window-size=1920x1080")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(20)
    yield chrome_driver
    chrome_driver.quit()
