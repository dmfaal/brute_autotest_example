# Комплексный тест-кейс, где для выполнения необходимо убедиться в отсутствии сущностей или удалить их


from helpers.base_url_method import get_base_url
from helpers.elements_stash import ID
from helpers.elements_stash import SOME_HEADER
from helpers.elements_stash import JSON
from helpers.get_entities import record_in_list
from helpers.get_entities import count_elements
from http import HTTPStatus
import requests
import json


class TestPostDeleteGoalsCalculates:
    def test_post_delete_goals_calculate(self):
        # preconditions
        create_goal_response = \
            requests.post(url=f"{get_base_url()}/{ID}/goal",
                          headers=SOME_HEADER,
                          json=JSON)
        assert create_goal_response.status_code == HTTPStatus.OK

        get_id = record_in_list()
        last_id = get_id[-1]
        create_calculates_response = \
            requests.post(url=f"{get_base_url()}/{ID}/goal/{last_id}/calculate",
                          headers=SOME_HEADER,
                          json=JSON)
        assert create_calculates_response.status_code == HTTPStatus.OK
        # test-case
        id_number = len(count_elements()) - 1
        response = requests.get(url=f"{get_base_url()}/{ID}",
                                headers=SOME_HEADER)
        last_calculate = \
            json.loads(response.content)['goals'][id_number]['quantityDirect']['calculates'][0]['id']
        update_calculates = \
            requests.delete(url=f"{get_base_url()}/{ID}/goal/{last_id}/calculate/"
                                f"{last_calculate}",
                            headers=SOME_HEADER,
                            json=JSON)
        assert update_calculates.status_code == HTTPStatus.OK

        delete_goal = \
            requests.delete(url=f"{get_base_url()}/{ID}/goal/{last_id}",
                            headers=SOME_HEADER,
                            json=JSON)
        assert delete_goal.status_code == HTTPStatus.OK
