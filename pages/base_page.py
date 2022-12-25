import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    url = 'https://example_url.com'

    def __init__(self, driver: WebDriver, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def open(self, url):
        self.driver.get(url)

    @allure.step('Wait for element visibility')
    def get_element(self, locator: tuple, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator), ' : '.join(locator))

    @allure.step('Click on element')
    def click_on(self, locator, timeout=5):
        self.get_element(locator, timeout=timeout).click()
