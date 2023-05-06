import json
from utils.cheking import Checking
from utils.api import StarWarsApi


"""Uploading a list of characters from films with Darth Vader to a file"""
class TestLoadListCharacters:
    def test_upload_list(self):

        # print("Method POST")
        # result_post = GoogleMapsApi.create_new_place()
        # check_post = result_post.json()
        # place_id = check_post.get("place_id")
        # Checking.check_status_code(result_post, 200)
        # Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # Checking.check_json_value(result_post, 'status', 'OK')

        print("Method GET")
        people = '/people/4/'
        result_get = StarWarsApi.get_upload_character(people)
        Checking.check_status_code(result_get, 200)
        # token = json.loads(result_get.text)   #  getting a list of fields
        # print(list(token))
        # Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
        #                                        'types', 'website', 'language'])
        # list_films = Checking.check_json_value(result_get, 'films', [
        # "https://swapi.dev/api/films/1/",
        # "https://swapi.dev/api/films/2/",
        # "https://swapi.dev/api/films/3/",
        # "https://swapi.dev/api/films/6/"
        # ])
        """Вытягиваем список фильмов в которых был персонаж Дарт Вейдер"""
        list_films = Checking.upload_json_value(result_get, 'films')
        #print(list_films)
        print(*list_films, sep='\n')
        person_name = Checking.upload_json_value(result_get, 'name')
        print(person_name)
        """Делаем мосив концов ссылок на фильмы для подстановки в метод"""
        list_film_names = [list_films[i][-9:] for i in range(len(list_films))]
        print(*list_film_names, sep='\n')


        """Вытягиваем перечень ссылок на персонажей по сслыке на фильм"""

        result_get = StarWarsApi.get_upload_character(list_film_names[0])

        """Делаем массив с концами ссылок персонажей для подстановки в готовый метод"""
        list_links_characters = [Checking.upload_json_value(result_get, 'characters')[i][-10:]
                                for i in range(len(Checking.upload_json_value(result_get, 'characters')))]

        print(*list_links_characters, sep='\n')

        # """Вытягиваем имена персонажей имея список концов ссылок"""
        #
        # result_get = StarWarsApi.get_upload_character(list_links_characters[0])
        # # list_people_names= [Checking.upload_json_value(result_get, 'name')[i]
        # #              for i in range(len(Checking.upload_json_value(result_get, 'name')))]
        # #
        # # print(*list_people_names)
        #
        # person_name = Checking.upload_json_value(result_get, 'name')
        # print(person_name)







        # print("Method PUT")
        # result_put = GoogleMapsApi.put_new_place(place_id)
        # Checking.check_status_code(result_put, 200)
        # Checking.check_json_token(result_put, ['msg'])
        # Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        #
        #
        # print("Method GET PUT")
        # result_get = GoogleMapsApi.get_new_place(place_id)
        # Checking.check_status_code(result_get, 200)
        # Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
        #                                        'types', 'website', 'language'])
        # Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')
        #
        # print("Method DELETE")
        # result_delete = GoogleMapsApi.delete_new_place(place_id)
        # Checking.check_status_code(result_delete, 200)
        # Checking.check_json_token(result_delete, ['status'])
        # Checking.check_json_value(result_delete, 'status', 'OK')
        #
        #
        # print("Method GET DELETE")
        # result_get = GoogleMapsApi.get_new_place(place_id)
        # Checking.check_status_code(result_get, 404)
        # Checking.check_json_token(result_get, ['msg'])
        # Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        # Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')
        #

        print("Testing uploading a list of characters from films with Darth Vader to a file has been completed successfully!!!")
