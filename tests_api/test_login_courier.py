import allure
from data import ApiEndpoints, AnswersLoginCourier
from helpers import Helpers
import requests


@allure.feature('Авторизация курьера')
class TestLoginCourier:


    @allure.title('Успешная авторизация')
    def test_login_courier_success(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(ApiEndpoints.LOGIN, data=payload)

        assert response.status_code == 200 and AnswersLoginCourier.login_courier_success in response.json()

    @allure.title('Попытка входа курьера с неверным паролем')
    def test_login_with_incorrect_password(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": 'wrong'
        }
        response = requests.post(ApiEndpoints.LOGIN, data=payload)
        assert 404 == response.status_code and AnswersLoginCourier.error_message_incorrect_password in response.text

    @allure.title('Попытка входа несуществующего пользователя')
    def test_login_non_existent_user(self):
        payload = {
            "login": 'nobody',
            "password": '10101'
        }
        response = requests.post(ApiEndpoints.LOGIN, data=payload)
        assert 404 == response.status_code and AnswersLoginCourier.error_message_non_existent_user in response.text

    @allure.title('Попытка авторизации пользователя без заполненного поля')
    def test_login_courier_missing_one_attribute(self):
        payload = {
            "password": '12345'
        }
        response = requests.post(ApiEndpoints.LOGIN, data=payload)
        assert 400 == response.status_code and AnswersLoginCourier.error_message_courier_missing_one_attribute in response.text

    @allure.title('Авторизация пользователя с возвратом ID при успешной аутентификации')
    def test_successful_request_return_id(self):
        helper = Helpers()
        login, password, first_name = helper.register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(ApiEndpoints.LOGIN, data=payload)
        assert "id" in response.text
