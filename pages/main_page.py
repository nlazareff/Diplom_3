import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Нажать на ссылку "Лента Заказов"')
    def click_order_list_link(self):
        return self.wait_and_click_element_by_script(MainPageLocators.ORDER_LIST_LINK)

    @allure.step('Нажать на ссылку "Конструктор"')
    def click_constructor_link(self):
        return self.wait_and_click_element_by_script(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Нажать на ингредиент "Флюоресцентная булка R2-D3"')
    def click_fluorescent_bun_link(self):
        return self.wait_and_click_element_by_script(MainPageLocators.FLUORESCENT_BUN_LINK)

    @allure.step('Проверить отображение заголовка "Детали ингредиента" в модальном окне')
    def ingredient_details_is_displaying(self):
        return self.is_element_displaying(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Нажать на крестик для закрытия окна с деталями ингредиента')
    def click_ingredient_modal_close(self):
        return self.wait_and_click_element_by_script(MainPageLocators.INGREDIENT_MODAL_CLOSE)

    @allure.step('Проверить, что заголовок модального окна "Детали ингредиента" не отображается')
    def ingredient_modal_is_not_displaying(self):
        return self.is_element_not_displaying(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Перетащить "Флюоресцентная булка R2-D3" в область заказа')
    def drag_ingredient_to_order(self):
        return self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN_LINK, MainPageLocators.CONSTRUCTOR_BASKET_TOP)

    @allure.step('Получить количество ингредиентов счётчика у "Флюоресцентная булка R2-D3"')
    def get_count_of_ingredients(self):
        return self.wait_and_get_text(MainPageLocators.COUNTER_FLUORESCENT_BUN)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_order_button(self):
        return self.wait_and_click_element_by_script(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_change_text(MainPageLocators.ORDER_MODAL_ID, "9999")
        return self.wait_and_get_text(MainPageLocators.ORDER_MODAL_ID)

    @allure.step('Нажать на крестик для закрытия окна с номером заказа')
    def click_order_modal_close(self):
        return self.wait_and_click_element_by_script(MainPageLocators.ORDER_MODAL_CLOSE)

    @allure.step('Оформить заказать')
    def create_order(self):
        self.drag_ingredient_to_order()
        self.click_order_button()
        order_number = self.get_order_number()
        self.click_order_modal_close()

        return order_number
