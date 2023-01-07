import json

from requests import Response
from api import GoogleMapsAPI
from cheking import Cheking

"""Create, update, delete new location """

class Test_create_place():
    """class for test api"""

    def test_create_new_place(self):

        print("Method POST")
        result_post = GoogleMapsAPI.create_new_place()
        place_id = result_post.json().get('place_id')
        Cheking.check_status_code(result_post, 200)
        chek_arr = json.loads(result_post.text)
        Cheking.check_json_token(result_post, list(chek_arr))
        print("Method GET")
        result_get = GoogleMapsAPI.get_new_place(place_id)

        print("Method PUT")
        result_put = GoogleMapsAPI.put_new_place(place_id)
        Cheking.check_json_token(result_put, ["msg"])
        print("Method GET")
        result_get = GoogleMapsAPI.get_new_place(place_id)

        print("Method DELETE")
        result_delete = GoogleMapsAPI.delete_place(place_id)
        check_delete_arr = json.loads(result_delete.text)
        Cheking.check_json_token(result_delete, list(check_delete_arr))
        print("Method GET")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)


