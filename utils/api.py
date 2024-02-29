from utils.http_methods_file import http_methods
import json

""""Методы для тестирования Google Maps API"""

base_url = 'https://rahulshettyacademy.com'  # Base URL - основная ссылка для google maps
parameters = '?key=qaclick123'  # Параметр для все запросов


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        post_path = '/maps/api/place/add/json'  # путь метода POST для API google maps
        post_url = base_url + post_path + parameters
        print(post_url)

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_result = http_methods.post(post_url, json_for_create_new_place)
        print(json.dumps(post_result.json(), indent=4))
        return post_result

    """Метод для проверки новой локации Google Maps"""

    @staticmethod
    def get_new_place(place_id):
        get_path = '/maps/api/place/get/json'
        get_url = base_url + get_path + parameters + '&place_id=' + place_id
        print(get_url)

        get_result = http_methods.get(get_url)
        print(json.dumps(get_result.json(), indent=4))
        return get_result

    """Обновления новой локации Google Maps"""

    @staticmethod
    def put_new_place(place_id):
        put_path = '/maps/api/place/update/json'
        put_url = base_url + put_path + parameters
        print(put_url)

        put_body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU (Updated)",
            "key": "qaclick123"
        }

        put_result = http_methods.put(put_url, put_body)
        print(json.dumps(put_result.json(), indent=4))
        return put_result

    """"Удаление локации"""
    @staticmethod
    def delete_place(place_id):

        delete_path = '/maps/api/place/delete/json'
        delete_url = base_url + delete_path + parameters
        print(delete_url)

        delete_body = {
            "place_id": place_id
        }

        delete_result = http_methods.delete(delete_url, delete_body)
        print(json.dumps(delete_result.json(), indent=4))
        return delete_result
