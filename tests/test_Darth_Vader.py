from utils.cheking import Checking
from utils.api import StarWarsApi


"""Uploading a list of characters from films with Darth Vader to a file"""


class TestLoadListCharacters:
    def test_upload_list(self):

        print("Method upload list/GET")
        people = '/people/4/'
        result_get = StarWarsApi.get_upload_data(people)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'name', 'Darth Vader')
        """Pull out the list of films in which the character Darth Vader was"""
        list_films = StarWarsApi.upload_json_value(result_get, 'films')
        print(*list_films, sep='\n')
        """Making a list of movie resources"""
        list_film_names = [list_films[i][21:] for i in range(len(list_films))]
        print(*list_film_names, sep='\n')  # print an array of resource links
        """Pulling the list of characters resources from the lists of movie"""
        links_characters = []
        for i in range(len(list_film_names)):
            result_get = StarWarsApi.get_upload_data(list_film_names[i])
            list_links_characters = [StarWarsApi.upload_json_value(result_get, 'characters')[i][21:] for i in
                                     range(len(StarWarsApi.upload_json_value(result_get, 'characters')))]
            links_characters.extend(list_links_characters)
        links_characters.sort()  # Sorting for preparation of removal of duplicates
        """Clean up the list of duplicates"""
        cleaned_list_links = [links_characters[0]]
        cleaned_list_links.extend([links_characters[i] for i in range(1, len(links_characters)) if links_characters[i]
                                   != links_characters[i-1]])
        print("List of unique links", *cleaned_list_links, sep='\n')
        """Pulling the names of the characters"""
        for i in range(len(cleaned_list_links)):
            result_get = StarWarsApi.get_upload_data(cleaned_list_links[i])
            person_name = StarWarsApi.upload_json_value(result_get, 'name')
            """Putting character names in a file"""
            fw = open('characters.txt', "a")
            fw.write(person_name + '\n')
            fw.close()

        print("Testing uploading a list of characters from films with Darth Vader to a file has been completed "
              "successfully!!!")
