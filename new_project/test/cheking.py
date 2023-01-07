"""Методы проверки ответов на запросы"""
import json

from requests import Response


class Cheking():
    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(request, status_code):

        #assert status_code == request.status_code, "WRONG ANSWER"
        if request.status_code == status_code:
            print(f"SUCCESS ٩(×̯×)۶ {request.status_code}")
        else:
            print("FAILED")

    """Метод для проверки наличия обязательных полей в ответе"""

    @staticmethod
    def check_json_token(request, expected_value):
        token = json.loads(request.text)
        print(token)
        assert list(token) == expected_value, "wrong anser"
        print("поля соответствуют")



