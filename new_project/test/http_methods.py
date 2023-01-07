import requests

from logger import Logger

"""Список http методов"""


class Http_methods:
    """Init class"""
    headers = {
        'Content-Type': 'application/json'
    }
    #cookie = ''

    @staticmethod
    def get(url):
        """http method GET"""
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_methods.headers)
        return result

    @staticmethod
    def post(url, body):
        """http method GET"""
        Logger.add_request(url, method="POST")
        result = requests.post(url, headers=Http_methods.headers, json=body)
        return result

    @staticmethod
    def put(url, body):
        """http method GET"""
        Logger.add_request(url, method="PUT")
        result = requests.put(url, headers=Http_methods.headers, json=body)
        return result

    @staticmethod
    def delete(url, body):
        """http method GET"""
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=Http_methods.headers, json=body)
        return result
