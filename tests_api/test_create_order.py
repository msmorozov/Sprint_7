import pytest
import json
import allure
import requests
from data import ApiEndpoints

@allure.feature('Создание заказа')
class TestMakeAnOrder:


    @pytest.mark.parametrize('colors',[
        ["BLACK"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title('Создание заказа с параметризацией при выборе самоката')
    def test_make_parameterization_order(self, colors):
        payload = {
            "firstName": "Робаут",
            "lastName": "Жиллиман",
            "address": "Ультрамара, 1",
            "metroStation": 3,
            "phone": "+7 921 351 19 19",
            "rentTime": 1,
            "deliveryDate": "2024-11-15",
            "comment": "Задолго до пришествия Империума королевством Ультрамар правил Робаут Жиллиман, последний король-воин Макрагга",
            "color": colors
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(ApiEndpoints.ORDER, data=json.dumps(payload), headers=headers)
        assert response.status_code == 201 and 'track' in response.json()