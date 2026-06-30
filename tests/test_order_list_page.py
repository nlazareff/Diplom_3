import allure

from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from urls import Urls


class TestOrderListPage:
    
    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа')
    @allure.description('Тест проверяет, что при создании нового заказа счетчик "Выполнено за все время" на странице ленты заказов увеличивается на 1')
    def test_orders_all_time_counter_increases_after_create_order(self, user_login):  
        driver = user_login

        main_page = MainPage(driver)
        main_page.wait_for_url_to_be(Urls.MAIN_URL)
        main_page.click_order_list_link()
        main_page.wait_for_url_to_be(Urls.ORDER_LIST_URL)

        order_list_page = OrderListPage(driver)
        start_count = order_list_page.get_count_of_orders_all_time()
        
        main_page.click_constructor_link()
        main_page.wait_for_url_to_be(Urls.MAIN_URL)
        main_page.create_order()
        main_page.click_order_list_link()
        main_page.wait_for_url_to_be(Urls.ORDER_LIST_URL)

        new_count = order_list_page.get_count_of_orders_all_time()
                
        assert int(new_count) == int(start_count) + 1, f"Counter not increased: expected {int(start_count) + 1}, but got {int(new_count)}"

    @allure.title('Проверка увеличения счетчика "Выполнено за все сегодня" при создании нового заказа')
    @allure.description('Тест проверяет, что при создании нового заказа счетчик "Выполнено за все сегодня" на странице ленты заказов увеличивается на 1')
    def test_orders_today_counter_increases_after_create_order(self, user_login):  
        driver = user_login

        main_page = MainPage(driver)
        main_page.wait_for_url_to_be(Urls.MAIN_URL)
        main_page.click_order_list_link()
        main_page.wait_for_url_to_be(Urls.ORDER_LIST_URL)

        order_list_page = OrderListPage(driver)
        start_count = order_list_page.get_count_of_orders_today()
     
        main_page.click_constructor_link()
        main_page.wait_for_url_to_be(Urls.MAIN_URL)
        main_page.create_order()
        main_page.click_order_list_link()
        main_page.wait_for_url_to_be(Urls.ORDER_LIST_URL)

        new_count = order_list_page.get_count_of_orders_today()
                
        assert int(new_count) == int(start_count) + 1, f"Counter not increased: expected {int(start_count) + 1}, but got {int(new_count)}"

    @allure.title('Проверка отображения номера оформленного заказа в разделе "В работе"')
    @allure.description('Тест проверяет, что после оформления заказа его номер появляется в разделе "В работе" на странице ленты заказов')
    def test_order_id_in_work_is_displaying(self, user_login):  
        driver = user_login

        main_page = MainPage(driver)
        main_page.wait_for_url_to_be(Urls.MAIN_URL)
        order_number = main_page.create_order()
        main_page.click_order_list_link()
        main_page.wait_for_url_to_be(Urls.ORDER_LIST_URL)

        order_list_page = OrderListPage(driver)
        order_number_in_work = order_list_page.get_id_order_in_work()
                
        assert int(order_number) == int(order_number_in_work), f"Expected order {order_number}, but got {order_number_in_work}"
