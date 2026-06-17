import allure

from pages.main_page import MainPage
from urls import Urls


class TestMainPage:
    
    @allure.title('Проверка перехода на главную страницу по клику на "Конструктор"')
    @allure.description('Тест проверяет, что клик по ссылке "Конструктор" возвращает пользователя на главную страницу')
    def test_constructor_link_navigate_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_list_link()
        main_page.wait_for_url_to_be(Urls.ORDER_LIST_URL)
        main_page.click_constructor_link()

        assert main_page.get_url() == Urls.MAIN_URL, f"Expected URL {Urls.MAIN_URL}, but got {main_page.get_url()}"

    @allure.title('Проверка перехода в раздел Лента заказов по клику на "Лента заказов"')
    @allure.description('Тест проверяет, что клик по ссылке "Лента заказов" перенаправляет пользователя в раздел Лента заказов')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_list_link()

        assert main_page.get_url() == Urls.ORDER_LIST_URL, f"Expected URL {Urls.ORDER_LIST_URL}, but got {main_page.get_url()}"

    @allure.title('Проверка отображения всплывающего окна с деталями при клике на ингредиент')
    @allure.description('Тест проверяет, что клик на ингредиент открывает всплывающее окно с подробной информацией о нем')
    def test_click_ingredient_opens_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_link()

        assert main_page.ingredient_details_is_displaying(), f"Expected ingredient details window, but it was not displayed"

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик')
    @allure.description('Тест проверяет, что всплывающее окно с деталями ингредиента закрывается при клике на крестик')
    def test_close_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_link()
        main_page.click_ingredient_modal_close()

        assert main_page.ingredient_modal_is_not_displaying(), f"Expected ingredient modal to be closed, but it is still displayed"

    @allure.title('Проверка увеличения счетчика булки при добавлении в заказ')
    @allure.description('Тест проверяет, что при перетаскивании булки в область заказа счетчик увеличивается на 2 '
                       '(так как верхняя и нижняя булки считаются за 2 ингредиента)'
                       )
    def test_add_ingredient_increases_counter_success(self, driver):
        main_page = MainPage(driver)
        start_count = main_page.get_count_of_ingredients()
        main_page.drag_ingredient_to_order()
        new_count = main_page.get_count_of_ingredients()
        
        assert int(new_count) == int(start_count) + 2, f"Counter not increased: expected {int(start_count) + 2}, but got {int(new_count)}"
