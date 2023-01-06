import requests

class GoogleMaps_Check():
    """Класс для проверки получения валидной и невалидной созданной локации"""

    def __init__(self):
        """Инициализаця атрибутов"""
        self.base_url = "https://rahulshettyacademy.com"
        self.delete_resource = "/maps/api/place/delete/json?"
        self.get_resource = "/maps/api/place/get/json?"
        self.key = 'key=qaclick123'

    def delete(self):
        with open('place_id_list.txt','r') as pl:
            place_id_list = pl.read().split()
            print(place_id_list)


