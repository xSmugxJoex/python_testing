<<<<<<< HEAD
from selenium import webdriver
import pytest
=======
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


>>>>>>> version_1


@pytest.fixture(scope='function')
def driver():
<<<<<<< HEAD
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

=======
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(20)
    yield chrome_driver
    chrome_driver.quit()
>>>>>>> version_1
