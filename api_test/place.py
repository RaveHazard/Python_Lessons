import requests


class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""
        base_url = "https://rahulshettyacademy.com"
        key = '?key=qaclick123'
        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
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
        result_post = requests.post(post_url, json=json_for_create_new_location)
        # print(result_post.status_code)
        if result_post.status_code == 200:
            print("Success request, new location created")
            print(result_post.text)
        else:
            print("Wrong request")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        place_id = check_post.get('place_id')
        print(place_id)
        """Проверка создания новой локации"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        get_response = requests.get(get_url)
        get_response.json()
        print(get_response.text)
        print(place_id)
        return place_id

    def update_location(self,place_id):
        """Обновляем параметры локации"""
        print('====================================\n++++++++++++++++++++++++++++++++++++')
        base_url = "https://rahulshettyacademy.com/"
        key = 'key=qaclick123'
        put_resource = 'maps/api/place/update/json?'
        put_url = base_url + put_resource + key
        json_for_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        response_put = requests.put(put_url, json=json_for_update_location)
        print(response_put.status_code)
        if response_put.status_code == 200:
            req_put = response_put.json()
            req_put_massage = req_put.get('msg')
            if req_put_massage == 'Address successfully updated':
                print("Update success")
            else:
                print("Что-то пошло не так.....")
        elif response_put.status_code == 404:
            print("Статус: 404. Ошибка, локация с таким place_id отсутствует")
        else:
            print("Что-то пошло не так.....")




new_place = Test_new_location()
test_loc = new_place.test_create_new_location()
new_place.update_location(test_loc)
new_place.update_location('')