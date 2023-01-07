import requests


class Star_Wars_Persons():
    """Class for sort persons of all films STAR WARS"""

    def __init__(self):
        """Init sefault attributest"""
        self.base_url = "https://swapi.dev/"
        self.dw_url = "api/people/4/"

    def get_all_films_with_dart_wader(self):
        """Получаем список всех фильмов с Дарт Вейдером"""
        dw_films_url = self.base_url + self.dw_url
        print(f"Хьюстон, приём. Иду на {dw_films_url}.....")
        get_all_films = requests.get(dw_films_url)
        dw_body = get_all_films.json()
        dw_films = dw_body.get("films")
        print("Такс.... я получил список всех фильмов с Дартом вейдером")
        return dw_films  # Возвращаю список фильмов, чтобы потом присвоить его переменной

    def get_all_persons_from_film(self, film_arr):
        """Получаем список всех персонажей, который участвовали в фильме"""
        all_characters = []
        print("А теперь самое время получить список всех персонажей....")
        for film_id in film_arr:  # идем по всему списку фильмов
            film_persons = requests.get(film_id)
            film_persons_json = film_persons.json()
            persons = film_persons_json.get("characters")  # достаем из каждого фильма его список персонажей
            for character in persons:
                all_characters.append(character)  # добавляю всех персонажей в одтельный список.
        return all_characters # возвращаю список всех персонажей всех фильмов.

        print("Готово, список персонажей я подгрузил...Передаю на обработку списка")

    def save_characters_in_file(self, character_list):
        character_sort_list = set(character_list)
        with open('characters.txt', 'w') as ch:
            for character in character_sort_list:
                ch.write(f"{character}\n")
        print("Список со всеми персонажами обработан, все они в файлике characters.txt")

dw = Star_Wars_Persons()
#dw.save_characters_in_file(dw.get_all_persons_from_film(dw.get_all_films_with_dart_wader()))
film_list = dw.get_all_films_with_dart_wader()
character_list = dw.get_all_persons_from_film(film_list)
dw.save_characters_in_file(character_list)
