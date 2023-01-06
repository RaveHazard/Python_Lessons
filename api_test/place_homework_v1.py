import requests


class GoogleMaps_Req():
    """Класс для получения информации с сервиса googlemaps"""

    def __init__(self):
        """инициализация атрибутов класса"""
        self.base_url = "https://rahulshettyacademy.com"
        self.post_resource = "/maps/api/place/add/json?"
        self.delete_resource = '/maps/api/place/delete/json?'
        self.get_resource = "/maps/api/place/get/json?"
        self.key = 'key=qaclick123'

    def create_point(self):
        """Создание новой локации"""
        for i in range(5):
            post_url = self.base_url + self.post_resource + self.key  # полный адрес для запроса новой локации
            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                },
                "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": ["shoe park", "shop"],
                "website": "http://google.com",
                "language": "French-IN"
            }
            post_req = requests.get(post_url, json=json_for_create_new_location)  # передаем запрос на сервис
            # assert post_req.status_code == 200, 'Wrong response'
            if post_req.status_code == 200:
                print("Request success.....")
                post_req_json = post_req.json()
                place_id = post_req_json.get('place_id')
                with open('place_id_list.txt', 'a') as pl:
                    add_place_id = pl.write(f"{place_id}\n")
                    print("New location created and save in place_id_list.txt")
            elif post_req.status_code == 404:
                print("Please check you json or url☹")
            else:
                "Wrong body json, or failed in service☹"

    def get_created_point_info(self):
        """Проверка наличия созданной локации"""
        with open('place_id_list.txt', 'r') as pl:
            place_id_list = pl.read().split()
        for place_id in place_id_list:
            # идем по списку из файла, выполняем запрос, проверяем что ответ соотв.
            print("\nRead file place_id_list.txt, and preparing get request")
            get_url = self.base_url + self.get_resource + self.key + '&place_id=' + place_id
            get_req = requests.get(get_url)
            if get_req.status_code == 200:
                # Если успешный ответ, можно сравнить полученные поля, но этого нет в задании
                # Поэтому просто убеждаемся что ответ 200
                print("GET request was successfuly sand")
                print("Your location correctly saved in service\n¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯\n")
                get_reg_json = get_req.json()
            if get_req.status_code == 404:
                print("Oh....this place_id doesn't exists ٩(×̯×)۶")

    def delete_place_id(self):
        """Отправим на сервис запрос удаления четных записей в файле"""
        delete_url = self.base_url + self.delete_resource + self.key
        with open('place_id_list.txt', 'r') as pl:
            place_id_list = pl.read().split()
            for place_id in place_id_list:
                # идем по списку всех сохраненных локаций
                if place_id_list.index(place_id) % 2 == 0 and place_id_list.index(place_id) != 0:
                    # Выбираем все четные записи и отправляем запрос
                    delete_json = {
                        "place_id":place_id
                    }
                    delete_req = requests.delete(delete_url, json=delete_json)
                    print("Delete request successfuly send ٩(×̯×)۶ ")
                    # Проверим корректноть ответа от сервиса
                    if delete_req.status_code == 200:
                        delete_req_json = delete_req.json()
                        delete_req_proof_access = delete_req_json.get('status')
                        if delete_req_proof_access == 'OK':
                            print('======== Place_id deleted processed ========')
                        else:
                            print('Please check you json or url☹')
                    elif delete_req.status_code == 404:
                        print("Delete operation failed, looks like the data doesn't exists☹")

    def get_chek_actual_locations(self):









check = GoogleMaps_Req()
check.create_point()
# check.get_created_point_info()
check.delete_place_id()
