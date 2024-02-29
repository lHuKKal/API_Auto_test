import json
from requests import Response



"""Методы для проверки запросов"""
class Checking:

    """"Проверка статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("ОШИБКА!!! Статус код = " + str(response.status_code))

    """Метод для проверки наличе полей в ответе запроса"""
    @staticmethod
    def check_existing_fields(response: Response, expected_result):
        fields = json.loads(response.text)
        assert list(fields) == expected_result
        print("Все поля присутствуют (Checking class)")

    """Метод содержание целых слов в полях""" #
    @staticmethod  # Не часто будет использоваться
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





