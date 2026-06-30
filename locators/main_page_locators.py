from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_LINK = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]')     # Конструктор
    ORDER_LIST_LINK = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')    # Лента Заказов
    FLUORESCENT_BUN_LINK = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')    # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_MODAL_TITLE = (By.XPATH, '//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10" '
                                          'and text()="Детали ингредиента"]')     # Заголовок "Детали ингредиента" в модальном окне
    INGREDIENT_MODAL_CLOSE = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')    # Крестик для закрытия окна с деталями ингредиента
    COUNTER_FLUORESCENT_BUN = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[@class="counter_counter__num__3nue1"]') # Счетчик у ингредиента "Флюоресцентная булка R2-D3"
    CONSTRUCTOR_BASKET_TOP = (By.XPATH, '//div[@class="constructor-element constructor-element_pos_top"]')    # Верхняя секция конструктора бургера
    ORDER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg" '
                                        'and text()="Оформить заказ"]')    # Кнопка "Оформить заказ"
    ORDER_MODAL_ID = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')    # Номер заказа в модальном окне
    ORDER_MODAL_CLOSE = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')    # Крестик для закрытия окна с номером заказа
