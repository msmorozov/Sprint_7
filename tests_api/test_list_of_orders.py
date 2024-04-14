import requests
import allure
from data import ApiEndpoints


class TestListOrder:
    @allure.feature("Тест: возврат списка заказов")
    @allure.title('Проверка возврата списка заказов в ответе')
    def test_list_order(self):
        request_url = ApiEndpoints.ORDER
        response = requests.get(request_url)
        assert response.status_code == 200
        assert "orders" in response.json() and isinstance(response.json()["orders"], list)
