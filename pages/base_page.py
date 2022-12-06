from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'http://meshok.net'

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_and_input(self, text: str, locator, time=10):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)).send_key(text)

    def find_and_click(self, locator, time=6):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def find_and_check_text(self, locator, text, time=4):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text))

    def find_pic(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    #def find_elements(self, args: tuple):
      #  by_name, by_val = args
      #  return self.driver.find_elements(by_name, by_val)

    def scroll_page(self):
        self.driver.execute_script('windows.scrollTo(0, document.body.scrollHeight);')

    def enter_by_text(self, args: tuple):
        by_name, by_val, text = args
        Select(self.driver.find_element(by_name, by_val)).select_by_visible_text(text)

    def enter_by_value(self, args: tuple):
        by_name, by_val, value = args
        Select(self.driver.find_element(by_name, by_val)).select_by_value(value)

    def actions_chains(self, args: tuple, args1: tuple):
        by_name, by_value = args
        # by_name1, by_value1 = args1
        return ActionChains(self.driver).move_to_element(self.driver.find_element(by_name, by_value)). \
            click().perform()#(self.driver.find_element(by_name1, by_value1)).perform()



