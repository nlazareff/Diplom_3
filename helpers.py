from faker import Faker
import allure
import requests

from urls import Urls


class FakeData:

    @staticmethod
    def generate_random_user_data():
        fake = Faker('ru_RU')
        
        return {
            "email": f"{fake.email()}",
            "password": f"{fake.password(length=10)}",
            "name": f"{fake.name()}"
        }

class UserApi:

    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(url=Urls.USER_CREATE_URL, json=body)

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(access_token):
        headers = {'Authorization': access_token}
        return requests.delete(url=Urls.USER_DELETE_URL, headers=headers)
