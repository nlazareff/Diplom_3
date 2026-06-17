import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_page(Urls.LOGIN_URL)

    @allure.step('Ввести email в поле Email')
    def input_email(self, email):
        self.wait_and_add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Ввести пароль в поле Пароль')
    def input_password(self, password):
        self.wait_and_add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_login_button(self):
        self.wait_and_click_element_by_script(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Авторизовать пользователя')
    def login_user(self, user_data):
        self.input_email(user_data["email"])
        self.input_password(user_data["password"])
        self.click_login_button()
