import allure
import pytest

from pages.registration_form_page import RegistrationFormPage


@allure.tag('ID 100')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form')
def test_send_reg_form(wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbus street 5')
    reg_page.input_additional_information('Additional test info')
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check positive names values')
@pytest.mark.parametrize("name", [pytest.param('BORIS', marks=pytest.mark.allure_label("ID 101", label_type="tag")),
                                   pytest.param(' Boris ',
                                                marks=pytest.mark.allure_label("ID 102", label_type="tag")),
                                   pytest.param('BoRis',
                                                marks=pytest.mark.allure_label("ID 103", label_type="tag")),
                                   pytest.param('Bo-ris',
                                                marks=pytest.mark.allure_label("ID 104", label_type="tag")),
                                   pytest.param('Bo ris',
                                                marks=pytest.mark.allure_label("ID 105", label_type="tag"))])
def test_send_reg_form_names(name, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name(name)
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbus street 5')
    reg_page.input_additional_information('Additional test info')
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check positive last name values')
@pytest.mark.parametrize("last_name", [pytest.param('BORIS', marks=pytest.mark.allure_label("ID 106", label_type="tag")),
                                   pytest.param(' Stogoff ',
                                                marks=pytest.mark.allure_label("ID 107", label_type="tag")),
                                   pytest.param('StoGoff',
                                                marks=pytest.mark.allure_label("ID 108", label_type="tag")),
                                   pytest.param('Sto-goff',
                                                marks=pytest.mark.allure_label("ID 109", label_type="tag")),
                                   pytest.param('Sto goff',
                                                marks=pytest.mark.allure_label("ID 110", label_type="tag"))])
def test_send_reg_form_last_name(last_name, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name(last_name)
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbus street 5')
    reg_page.input_additional_information('Additional test info')
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check positive company values')
@pytest.mark.parametrize("company", [pytest.param('MYCOMPANY', marks=pytest.mark.allure_label("ID 111", label_type="tag")),
                                   pytest.param(' Myconpany ',
                                                marks=pytest.mark.allure_label("ID 112", label_type="tag")),
                                   pytest.param('MyCompany',
                                                marks=pytest.mark.allure_label("ID 113", label_type="tag")),
                                   pytest.param('My-Company',
                                                marks=pytest.mark.allure_label("ID 114", label_type="tag")),
                                   pytest.param('My company',
                                                marks=pytest.mark.allure_label("ID 115", label_type="tag"))])
def test_send_reg_form_correct_company_values(company, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company(company)
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbus street 5')
    reg_page.input_additional_information('Additional test info')
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check positive business area values')
@pytest.mark.parametrize("business_area", [pytest.param('CONSTRUCTION', marks=pytest.mark.allure_label("ID 106", label_type="tag")),
                                   pytest.param(' Construction ',
                                                marks=pytest.mark.allure_label("ID 107", label_type="tag")),
                                   pytest.param('ConStruction',
                                                marks=pytest.mark.allure_label("ID 108", label_type="tag")),
                                   pytest.param('Con-Struction',
                                                marks=pytest.mark.allure_label("ID 109", label_type="tag")),
                                   pytest.param('Con Ctruction',
                                                marks=pytest.mark.allure_label("ID 110", label_type="tag"))])
def test_send_reg_form_correct_business_area_values(business_area, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area(business_area)
    reg_page.select_employees()
    reg_page.input_street('Columbus street 5')
    reg_page.input_additional_information('Additional test info')
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check correct street values')
@pytest.mark.parametrize("street", [pytest.param('STREET', marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(' Street ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('StReet',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('Str-eet',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('Str eet',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_correct_street_values(street, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street(street)
    reg_page.input_additional_information('Additional test info')
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check correct additional info values')
@pytest.mark.parametrize("additional_info", [pytest.param('ADINFO', marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(' Adinfo ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('AdInfo',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('Ad-info',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('Ad info',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_correct_info_values(additional_info, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbis street 5')
    reg_page.input_additional_information(additional_info)
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check correct zip code values')
@pytest.mark.parametrize("zip_code", [pytest.param(6027, marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param( 6027 ,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(60276027,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(6027602760276027,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_correct_zip_code_values(zip_code, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbis street 5')
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(zip_code)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check correct phone code values')
@pytest.mark.parametrize("phone_code", [pytest.param('+3', marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('+ 3 ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(' +3 ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('+333',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_correct_phone_code_values(phone_code, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbis street 5')
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(6027)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code(phone_code)
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check correct phone values')
@pytest.mark.parametrize("phone", [pytest.param('8888888888 ', marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(' 8888888888',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(' 8888888888 ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('8888 888888',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_correct_phone_values(phone, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbis street 5')
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(6027)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number(phone)
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check correct email values')
@pytest.mark.parametrize("email", [pytest.param(' test@email.com ', marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(' test@email.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@email.com ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@ema-il.com ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('te-st@email.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_correct_phone_values(email, wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
    reg_page.select_employees()
    reg_page.input_street('Columbis street 5')
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(6027)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email(email)
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_success_message('Success example message')
