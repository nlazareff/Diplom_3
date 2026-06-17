from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_FIELD = (By.XPATH, '//label[text() = "Email"]/following-sibling::input')    # Поле "Email" в форме авторизации
    PASSWORD_FIELD = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')    # Поле "Пароль" в форме авторизации
    LOGIN_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" '
                                        'and text()="Войти"]')    # Кнопка "Войти" в форме авторизации
