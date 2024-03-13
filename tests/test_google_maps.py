import json
import allure

import response
from requests import Response
from utils.api import GoogleMapsApi
from utils.Checking import Checking
from utils.Checking import GetValue

"""Создание, изменение, удаление новой локации"""


@allure.epic("Test Create New Location")  # Глобальный Allure, его надо ставить перед КАЖДЫМ классом
class TestCreatePlace:

    @allure.description("CRUD New Location")  # Test Suit Allure, его необходимо ставить перед функцией с описанием данного тест плана
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()

        check_post = result_post.json()
        place_id = GetValue.get_value_from_field(result_post, 'place_id')
        print('переменная - ' + str(place_id))
        # place_id = check_post.get("place_id")

        Checking.check_status_code(result_post, 200)
        Checking.check_existing_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_contains_field(result_post, 'status', 'OK')

        # fields = json.loads(result_post.text)  # получить список полей ЛАЙФАК
        # print(list(fields))

        print("Метод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)  # Проверка, что локация была создана методом POST

        Checking.check_status_code(result_get, 200)
        Checking.check_existing_fields(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_contains_field(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        Checking.check_existing_fields(result_put, ['msg'])

        print("Метод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)  # Проверка, что данные обновились методом PUT

        Checking.check_status_code(result_put, 200)
        Checking.check_existing_fields(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_contains_field(result_get, 'address', '100 Lenina street, RU (Updated)')

        print("Метод DELETE")
        result_delete: Response = GoogleMapsApi.delete_place(place_id)  # Удаление созданной локации

        Checking.check_status_code(result_delete, 200)
        Checking.check_existing_fields(result_delete, ['status'])

        print("Метод GET DELETE")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)  # Проверка, что данные удалились методом DELETE

        Checking.check_status_code(result_get, 404)
        Checking.check_existing_fields(result_get, ['msg'])
        Checking.check_value_in_the_field(result_get, 'msg', 'failed')

        print('Тестирование создание/редактирование/удаление новой локации завершено УСПЕШНО')

# Команда для запуска тестов - python -m pytest -s -v
# Команда запуска для теста с allure - python -m pytest --alluredir=test_result/ tests/test_google_maps.py (путь создания)
