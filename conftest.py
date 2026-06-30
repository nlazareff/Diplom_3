import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.login_page import LoginPage
from helpers import FakeData, UserApi
from urls import Urls


@pytest.fixture(scope="function", params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'chrome':
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()

    elif request.param == 'firefox':
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()

    browser.get(Urls.MAIN_URL)

    yield browser

    browser.quit()

@pytest.fixture(scope="function")
def user_create():
    user_data = FakeData.generate_random_user_data()
    response = UserApi.create_user(user_data)
    
    access_token = None
    if response.status_code == 200:
        access_token = response.json().get('accessToken')

    yield user_data, access_token
    
    if access_token is not None:
        UserApi.delete_user(access_token) 

@pytest.fixture(scope="function")
def user_login(driver, user_create):
    user_data, _ = user_create
    
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_user(user_data)

    return driver
