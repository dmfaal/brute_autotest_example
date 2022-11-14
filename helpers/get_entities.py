# Записать в список


from helpers.base_url_method import get_base_url
from helpers.elements_stash import SOME_HEADER
import requests


def record_in_list():
    response = requests.get(url=f"{get_base_url()}",
                            headers=SOME_HEADER)
    return [rec['ids'] for rec in response.json()['entities']]


def count_elements():
    return len(record_in_list())
