import allure

from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListPageLocators


class OrderListPage(BasePage):
    
    @allure.step('Получить количество заказов счетчика "Выполнено за все время"')
    def get_count_of_orders_all_time(self):
        return self.wait_and_get_text(OrderListPageLocators.COUNTER_ORDERS_ALL_TIME)

    @allure.step('Получить количество заказов счетчика "Выполнено за сегодня"')
    def get_count_of_orders_today(self):
        return self.wait_and_get_text(OrderListPageLocators.COUNTER_ORDERS_TODAY)

    @allure.step('Получить номер заказа, который находится в разделе "В работе"')
    def get_id_order_in_work(self):
        self.wait_change_text(OrderListPageLocators.ORDER_ID_IN_WORK, "Все текущие заказы готовы!")
        return self.wait_and_get_text(OrderListPageLocators.ORDER_ID_IN_WORK)
