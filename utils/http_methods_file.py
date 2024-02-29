import allure
import requests

from utils.logger import Logger

"""Список HTTP методов"""


class http_methods():
    headers = {'content-type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step("GET"):  # к методу подключен Allure и можно добавить описание данного запроса
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def patch(url, body):
        with allure.step("PATCH"):
            Logger.add_request(url, method="PATCH")
            result = requests.patch(url, json=body, headers=http_methods.headers, cookies=http_methods.cookie)
            Logger.add_response(result)
            return result
