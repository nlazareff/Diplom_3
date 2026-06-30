from selenium.webdriver.common.by import By


class OrderListPageLocators:

    COUNTER_ORDERS_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')    # Счетчик "Выполнено за все время" 
    COUNTER_ORDERS_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')    # Счетчик "Выполнено за сегодня"
    ORDER_ID_IN_WORK = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]'
                                  '/li[contains(@class, "text_type_digits-default")]')    # Номер заказа в разделе "В работе"
