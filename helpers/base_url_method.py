# метод добычи base_url для использования если в env url отсутствует


import os

BASE_URL = "https://my-url.ru"


def get_base_url():
    if os.getenv('BASE_URL') is not None:
        base_url = os.getenv('BASE_URL')
        return base_url
    else:
        return BASE_URL


