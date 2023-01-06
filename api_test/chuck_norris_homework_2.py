import requests


class TakeChuckNorrisJokes():
    """Параметры класса для получения нужной шутки от чака"""

    def __init__(self):
        """инициализируем параметры(их нет)"""
        pass

    def chose_and_check_category(self):
        """Получение категории шутки от Чака"""
        print("Загружаем список убойных шуток от чака.......")
        category_url = 'https://api.chucknorris.io/jokes/categories'
        category_req = requests.get(category_url)
        if category_req.status_code == 200:
            category_req_list = category_req.json()
            user_category = input("Отлично, список убойных шуток загружен\nВедите категорию шутки от Чака: ")
            if user_category.lower() in category_req_list:
                # Проверяем наличие выбранной категории в полученном списке
                return user_category
            else:
                return False
        else:
            print("Что-то пошло не так.....")
            return False

    def take_chucks_joke(self, user_category):
        """Вывод шутки на выбранную ранее тему"""
        if user_category != False:
            joke_url = 'https://api.chucknorris.io/jokes/random?category=' + user_category
            joke_req = requests.get(joke_url)
            joke_req_json = joke_req.json()
            joke = joke_req_json.get('value')
            print(f'Шутка от Чака: {joke}')
        else:
            print("Либо такой категории нет, либо что-то пошло не так.....")


joke = TakeChuckNorrisJokes()
category = joke.chose_and_check_category()
joke.take_chucks_joke(category)
#joke.take_chucks_joke(joke.chose_category())
