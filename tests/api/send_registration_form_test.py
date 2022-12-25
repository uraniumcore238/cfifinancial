import os
import allure
import requests
from dotenv import load_dotenv
from pytest_voluptuous import S
from schemas import registration_schema


@allure.tag('ID 1')
@allure.severity(severity_level='normal')
@allure.story('API tests')
@allure.suite('')
@allure.title('')
def test_send_registration_form():
    load_dotenv()
    base_url = f'https://{os.getenv("BASE_DOMAIN")}'
    session = requests.Session()
    end_point = f'{base_url}/api/example'
    parameters = {
                        "title": 'mr',
                        "firstName": 'Boris',
                        "lastName": 'Stogoff',
                        'position': 'employee_1',
                        'company': 'My Company',
                        'businesArea': 'Construction',
                        'employees': 'example_employee_1',
                        'street': 'Columbus street',
                        'additionalInformation': 'additionat test information',
                        'zipCode': 6027,
                        'place': 'example_place_1',
                        'Country': 'Cyprus',
                        'code': '+7',
                        'phone_number': '8888888888',
                        'your_email': 'test@emai.com',
                        'termsAccept': True
    }
    registration = session.post(url=end_point, json=parameters, timeout=10)
    assert registration.status_code == 200
    assert S(registration_schema) == registration.json()


@allure.tag('ID 2')
@allure.severity(severity_level='normal')
@allure.story('API tests')
@allure.suite('')
@allure.title('')
def test_send_empty_registration_form():
    load_dotenv()
    base_url = f'https://{os.getenv("BASE_DOMAIN")}'
    session = requests.Session()
    end_point = f'{base_url}/api/example'
    parameters = {
                        "title": '',
                        "firstName": '',
                        "lastName": '',
                        'position': '',
                        'company': '',
                        'businesArea': '',
                        'employees': '',
                        'street': '',
                        'additionalInformation': '',
                        'zipCode': None,
                        'place': '',
                        'Country': '',
                        'code': '',
                        'phone_number': '',
                        'your_email': '',
                        'termsAccept': None
    }
    registration = session.post(url=end_point, json=parameters, timeout=10)
    assert registration.status_code == 404


@allure.tag('ID 3')
@allure.severity(severity_level='normal')
@allure.story('Api tests')
@allure.suite('')
@allure.title('')
def test_send_registration_form_no_tems():
    load_dotenv()
    base_url = f'https://{os.getenv("BASE_DOMAIN")}'
    session = requests.Session()
    end_point = f'{base_url}/api/example'
    parameters = {
                        "title": 'mr',
                        "firstName": 'Boris',
                        "lastName": 'Stogoff',
                        'position': 'employee_1',
                        'company': 'My Company',
                        'businesArea': 'Construction',
                        'employees': 'example_employee_1',
                        'street': 'Columbus street 5',
                        'additionalInformation': 'additionat test information',
                        'zipCode': 6027,
                        'place': 'example_place_1',
                        'Country': 'Cyprus',
                        'code': '+7',
                        'phone_number': '8888888888',
                        'your_email': 'test@emai.com',
                        'termsAccept': None
    }
    registration = session.post(url=end_point, json=parameters, timeout=10)
    assert registration.status_code == 404
   
