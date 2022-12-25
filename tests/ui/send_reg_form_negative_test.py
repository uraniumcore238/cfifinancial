import allure
import pytest

from pages.registration_form_page import RegistrationFormPage


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid names values')
@pytest.mark.parametrize("name", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 101", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@test.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_names(name, wd):
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
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Check positive last name values')
@pytest.mark.parametrize("last_name", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 106", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@test.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form(last_name, wd):
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
    reg_page.assert_warning_message('Warning example message')


@allure.tag('ID ')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Empty title')
def test_send_reg_form_empty_title(wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
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
    reg_page.assert_warning_message('Warning example message')


@allure.tag('ID ')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Empty position')
def test_send_reg_form_empty_position(wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
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
    reg_page.assert_warning_message('Warning example message')


@allure.tag('ID ')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Empty employees')
def test_send_reg_form_empty_employees(wd):
    reg_page = RegistrationFormPage(wd)
    reg_page.open('')
    reg_page.select_title()
    reg_page.input_first_name('Boris')
    reg_page.input_last_name('Stogoff')
    reg_page.select_position()
    reg_page.input_company('My company')
    reg_page.business_area('Construction')
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
    reg_page.assert_warning_message('Warning example message')


@allure.tag('ID ')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Empty place')
def test_send_reg_form_empty_place(wd):
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
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.tag('ID ')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Empty country')
def test_send_reg_form_empty_country(wd):
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
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.tag('ID ')
@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Checkbox not checked')
def test_send_reg_form_checkbox_not_checked(wd):
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
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid company values')
@pytest.mark.parametrize("company", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@test.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_company(company, wd):
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
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid business area values')
@pytest.mark.parametrize("business_area", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@test.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_business_area(business_area, wd):
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
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid street values')
@pytest.mark.parametrize("street", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@test.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_street(street, wd):
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
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid additional info values')
@pytest.mark.parametrize("ad_info", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))
                                  ])
def test_send_reg_form_invalid_ad_info(ad_info, wd):
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
    reg_page.input_additional_information(ad_info)
    reg_page.input_zip_code(6287)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid zip code values')
@pytest.mark.parametrize("zip_code", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),

                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_zip_code(zip_code, wd):
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
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(zip_code)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid phone code values')
@pytest.mark.parametrize("phone_code", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('+',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(123456789,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_phone_code(phone_code, wd):
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
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(6027)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code(phone_code)
    reg_page.input_phone_number('8888888888')
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid phone number values')
@pytest.mark.parametrize("phone_number", [pytest.param('АБВГДУ', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('+',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('sdfsdfsdf',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                    pytest.param('8-8-8-8-8-8-8-8-8',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param(12345678988888888,
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_phone(phone_number, wd):
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
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(6027)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number(phone_number)
    reg_page.input_email('test@test.com')
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')


@allure.severity(severity_level='normal')
@allure.story('Example story')
@allure.suite('Example suite')
@allure.title('Send registration form. Invalid email values')
@pytest.mark.parametrize("email", [pytest.param('АБВГДУ@mail.com', marks=pytest.mark.allure_label("ID 122", label_type="tag")),
                                   pytest.param('!"№;%:?*()_+<>?":*@mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('<script>alert</script>@mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('          ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('+@mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('sdfs dfsdf@mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                    pytest.param('        ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@@mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('testmail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@.mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@ma il.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail .com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mailcom',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@ mail .com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail.',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail..com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail.com.',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail.co.m',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail.co m',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail. com ',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('тест@mail.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@мэйл.com',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('test@mail.ком',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag")),
                                   pytest.param('',
                                                marks=pytest.mark.allure_label("ID ", label_type="tag"))])
def test_send_reg_form_invalid_phone(email, wd):
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
    reg_page.input_additional_information('Additional info')
    reg_page.input_zip_code(6027)
    reg_page.select_place()
    reg_page.select_country()
    reg_page.input_phone_code('+3')
    reg_page.input_phone_number('8888888888')
    reg_page.input_email(email)
    reg_page.check_checkbox()
    reg_page.click_on_register_button()
    reg_page.assert_warning_message('Warning example message')