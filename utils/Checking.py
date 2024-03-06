import json
from requests import Response

"""Методы для проверки запросов"""


class Checking:
    """"Проверка статус кода"""

    @staticmethod  # Обязательная проверка на статус !!
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("ОШИБКА!!! Статус код = " + str(response.status_code))

    """Метод для проверки наличе полей в ответе запроса"""

    @staticmethod  # ОЧЕНЬ редкая проверка списка полей в ответе
    def check_existing_fields(response: Response, expected_result):
        fields = json.loads(response.text)
        assert list(fields) == expected_result
        print("Все поля присутствуют (Checking class)")

    """Метод содержание целых слов в полях"""

    @staticmethod  # Не часто будет использоваться !!!!
    def check_contains_field(response: Response, field_name, expected_result):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_result
        print(field_name + ' значение верно')

    """Проверка по заданному слову которая присутствует в поле"""

    @staticmethod
    def check_value_in_the_field(response: Response, field_name, expected_word):
        check = response.json()
        check_info = check.get(field_name)
        if expected_word in check_info:
            print('Слово ' + expected_word + ' присутствует в поле!!!')
        else:
            print('Слово ' + expected_word + ' не присутствует в поле!!!')


class GetValue:

    """"Берем значение из указанного поля"""
    @staticmethod
    def get_value_from_field(response: Response, extract_field_name):
        check = response.json()
        check_info = check.get(extract_field_name)
        return check_info

    """"Берем значение указанного поля из указанного индекса объекта полученного списка"""
    @staticmethod
    def get_value_from_item_of_list(response: Response, field_of_list, index, take_value_from_field):
        response_check = response.json()
        first_index_value_from_list = response_check.get(field_of_list, [])[index]
        take_value_from_field = first_index_value_from_list.get(take_value_from_field)
        return take_value_from_field
