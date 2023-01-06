import requests


class Test_Chuck_Norris_joke():
    """Class for take Chuk's jokes"""

    def __init__(self):
        self.url = 'https://api.chucknorris.io/jokes/'
        pass

    def take_all_categories(self):
        """Method for take all category jokes list"""
        category_url = self.url + 'categories'
        category = requests.get(category_url)
        # Есть ли смысл тут проверять ассертом, если ниже я могу отсеять все другие коды ошибок?
        if category.status_code == 200:
            print("Success request")
            category_list_json = category.json()
            print("Доступны следующие котегории шуток:")
            for categories in category_list_json:
                print(f"- категория {categories}")
            return category_list_json
        else:
            print("Wrong request")

    def take_all_categories_joke(self, category_list):
        """Method for take  1 random jokes from all categories"""
        for choose_category in category_list:
            print(f"Ожидаем шутку из категории {choose_category.title()}")
            jokes_url = 'https://api.chucknorris.io/jokes/random?category=' + choose_category
            joke_req = requests.get(jokes_url)
            # Есть ли смысл тут проверять ассертом, если ниже я могу отсеять все другие коды ошибок?
            if joke_req.status_code == 200:
                print("Success request")
                joke_req_json = joke_req.json()
                joke = joke_req_json.get('value')
                if "chuck norris" in joke.lower():
                    print(f"Шутка на выбранную категорию:\n{joke}")
                    print("=========================================")
                else:
                    print("Какая то странная шутка, она не про Чака")
            else:
                print("Сервис не отвечает :(")


test_joke = Test_Chuck_Norris_joke()
category_list = test_joke.take_all_categories()
test_joke.take_all_categories_joke(category_list)
#test_joke.take_all_categories_joke(test_joke.take_all_categories())
