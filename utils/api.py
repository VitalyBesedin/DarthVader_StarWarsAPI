from utils.http_methods import HttpMethods
"""Methods for Testing Star Wars API"""
base_url = "https://swapi.dev/api"     # Base URL


class StarWarsApi:

    """Method for uploading Star Wars characters"""

    @staticmethod
    def get_upload_data(add_url):
        get_url = base_url + add_url
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for loading values from requested fields"""

    @staticmethod
    def upload_json_value(result, field_name):
        check = result.json()
        check_info = check.get(field_name)
        """ return value"""
        return check_info
