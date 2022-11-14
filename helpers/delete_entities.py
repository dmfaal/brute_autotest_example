# хелпер который парсит и удаляет все сущности


from helpers.base_url_method import get_base_url
from helpers.elements_stash import ID
from helpers.elements_stash import SOME_HEADER
from helpers.elements_stash import JSON
from helpers.get_entities import record_in_list
from helpers.get_entities import count_elements
from http import HTTPStatus
import requests
import itertools


class TestDeleteAll:
    def test_delete_all(self):
        id_numbers = count_elements()
        if len(id_numbers) != 0:
            run_list = itertools.cycle(id_numbers)
            next(run_list)
            id_amount = len(record_in_list())
            for i in range(id_amount):
                next_element = next(run_list)
                if not next_element:
                    pass
                else:
                    response = requests.delete(url=f"{get_base_url()}/{ID}/goal/{next_element}",
                                               headers=SOME_HEADER,
                                               json=JSON)
                    assert response.status_code == HTTPStatus.OK
        else:
            pass
