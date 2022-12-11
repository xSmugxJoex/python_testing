from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
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
            EC.visibility_of_element_located(locator)).send_keys(text)

    def find_and_click(self, locator, time=6):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def find_pic(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    def color_verify(self, locator, arg: str):
        return self.find_element(locator).value_of_css_property(arg)

    def scroll_page(self):
        self.driver.execute_script('windows.scrollTo(0, document.body.scrollHeight);')

    def enter_by_text(self, args: tuple):
        by_name, by_val, text = args
        Select(self.driver.find_element(by_name, by_val)).select_by_visible_text(text)

    def enter_by_value(self, args: tuple):
        by_name, by_val, value = args
        Select(self.driver.find_element(by_name, by_val)).select_by_value(value)

    def switch_to_windows(self, arg: int):
        return self.driver.switch_to.window(self.driver.window_handles[arg])



