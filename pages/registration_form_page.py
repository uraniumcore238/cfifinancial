import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationFormPage(BasePage):

    TITLE_SELECTOR = (By.CSS_SELECTOR, ".example")
    MR_TITLE_SELECTOR = (By.CSS_SELECTOR, ".example")
    MRS_TITLE_SELECTOR = (By.CSS_SELECTOR, ".example")
    FIRST_NAME = (By.CSS_SELECTOR, ".example")
    LAST_NAME = (By.CSS_SELECTOR, ".example")
    POSITION = (By.CSS_SELECTOR, ".example")
    EXAMPLE_POSITION = (By.CSS_SELECTOR, ".example")
    COMPANY = (By.CSS_SELECTOR, ".example")
    BUSINESS_AREA = (By.CSS_SELECTOR, ".example")
    EMPLOYEES = (By.CSS_SELECTOR, ".example")
    EMPLOYEES_EXAMPLE = (By.CSS_SELECTOR, ".example")
    STREET_AND_NR = (By.CSS_SELECTOR, ".example")
    ADDITIONAL_INFO = (By.CSS_SELECTOR, ".example")
    ZIP_CODE = (By.CSS_SELECTOR, ".example")
    PLACE = (By.CSS_SELECTOR, ".example")
    PLACE_EXAMPLE = (By.CSS_SELECTOR, ".example")
    COUNTRY_SELECTOR = (By.CSS_SELECTOR, ".example")
    COUNTRY_EXAMPLE = (By.CSS_SELECTOR, ".example")
    CODE = (By.CSS_SELECTOR, ".example")
    PHONE_NUMBER = (By.CSS_SELECTOR, ".example")
    YOUR_EMAIL = (By.CSS_SELECTOR, ".example")
    TERMS_CHECKBOX = (By.CSS_SELECTOR, ".example")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".example")
    TERMS_LINK = (By.CSS_SELECTOR, ".example")
    TERMS_TEXT_BLOCK = (By.CSS_SELECTOR, ".example")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".example")
    WARNING_MESSAGE = (By.CSS_SELECTOR, ".example")

    @allure.step('Select title')
    def select_title(self):
        self.click_on(self.TITLE_SELECTOR)
        self.get_element(self.MR_TITLE_SELECTOR).click()

    @allure.step('Input First Name')
    def input_first_name(self, name):
        self.get_element(self.FIRST_NAME).send_keys(name)

    @allure.step('Input Last Name')
    def input_last_name(self, last_name):
        self.get_element(self.LAST_NAME).send_keys(last_name)

    @allure.step('Select position')
    def select_position(self):
        self.click_on(self.POSITION)
        self.get_element(self.EXAMPLE_POSITION).click()

    @allure.step('Input company name')
    def input_company(self, company):
        self.get_element(self.COMPANY).send_keys(company)

    @allure.step('Input business area')
    def business_area(self, business_area):
        self.get_element(self.BUSINESS_AREA).send_keys(business_area)

    @allure.step('Select employees')
    def select_employees(self):
        self.click_on(self.EMPLOYEES)
        self.get_element(self.EMPLOYEES_EXAMPLE).click()

    @allure.step('Input street')
    def input_street(self, street):
        self.get_element(self.STREET_AND_NR).send_keys(street)

    @allure.step('Input additional information')
    def input_additional_information(self, info):
        self.get_element(self.ADDITIONAL_INFO).send_keys(info)

    @allure.step('Input zip code')
    def input_zip_code(self, zip_code):
        self.get_element(self.ZIP_CODE).send_keys(zip_code)

    @allure.step('Select place')
    def select_place(self):
        self.click_on(self.PLACE)
        self.get_element(self.PLACE_EXAMPLE).click()

    @allure.step('Select country')
    def select_country(self):
        self.click_on(self.COUNTRY_SELECTOR)
        self.get_element(self.COUNTRY_EXAMPLE).click()

    @allure.step('Input code')
    def input_phone_code(self, code):
        self.get_element(self.CODE).send_keys(code)

    @allure.step('Input phone number')
    def input_phone_number(self, phone_number):
        self.get_element(self.PHONE_NUMBER).send_keys(phone_number)

    @allure.step('')
    def input_email(self, email):
        self.get_element(self.YOUR_EMAIL).send_keys(email)

    @allure.step('Check checkbox')
    def check_checkbox(self):
        self.click_on(self.TERMS_CHECKBOX)

    @allure.step('Click on register button')
    def click_on_register_button(self):
        self.click_on(self.REGISTER_BUTTON)

    @allure.step('Assert success message')
    def assert_success_message(self, expected_text):
        success_text = self.get_element(self.SUCCESS_MESSAGE).text
        assert success_text == expected_text, f'The resulting text "{success_text}" does not match the expected one "{expected_text}"'

    @allure.step('Assert warning message')
    def assert_warning_message(self, expected_text):
        success_text = self.get_element(self.WARNING_MESSAGE).text
        assert success_text == expected_text, f'The resulting text "{success_text}" does not match the expected one "{expected_text}"'