import requests


class TestNewJoke():
    """Create new joke"""

    def __init__(self):
        """init class """
        pass

    def test_create_new_joke(self):
        """create new random joke """
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        print("Status code " + str(response.status_code))
        assert 200 == response.status_code, "qweqeqw"
        if response.status_code == 200:
            print("Success, we take new joke")
        else:
            print("Filed, request failed")
        response.encoding = 'utf-8'
        print(response.text)
        check = response.json()
        check_info = check.get("categories")
        check_joke = check.get("value")
        print(check_info)
        assert check_info == []
        print("ok")
        if "chuck norris" in check_joke.lower():
            print(check_joke)
        else:
            print("joke not content Chuck Norris")

    def test_create_new_category_joke(self, category):
        """Create new joke in category"""
        url = 'https://api.chucknorris.io/jokes/random?category=' + category
        response = requests.get(url)
        if response.status_code != 404:
            assert response.status_code == 200
            print("status code: " + str(response.status_code))
            joke_json = response.json()
            joke = joke_json.get("value")
            if "chuck norris" in joke.lower():
                print(joke)
            else:
                print("failed")
        else:
            print("wrong category")




random_joke = TestNewJoke()
#random_joke.test_create_new_joke()
random_joke.test_create_new_category_joke('animal1')
