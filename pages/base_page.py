import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Config


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        return self.driver.get(url)
    
    @allure.step('Получить текущий URL')
    def get_url(self):
        return self.driver.current_url
    
    @allure.step('Подождать, пока URL станет равен ожидаемому URL')
    def wait_for_url_to_be(self, url):
        WebDriverWait(self.driver, Config.DEFAULT_TIME_WAITER).until(EC.url_to_be(url))
        return self.driver.current_url
        
    @allure.step('Подождать и найти элемент на странице')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIME_WAITER).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
 
    @allure.step('Подождать элемент на странице и кликнуть на него')
    def wait_and_click_element_by_script(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIME_WAITER).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Подождать и получить текст в элементе')
    def wait_and_get_text(self, locator):
        return self.wait_and_find_element(locator).text
    
    @allure.step('Подождать смены текста в элементе')
    def wait_change_text(self, locator, value):
        return WebDriverWait(self.driver, Config.DEFAULT_TIME_WAITER).until_not(EC.text_to_be_present_in_element(locator, value))
    
    @allure.step('Подождать элемент на странице и ввести в него текст')
    def wait_and_add_text_to_element(self, locator, text):
        return self.wait_and_find_element(locator).send_keys(text)
   
    @allure.step('Проверить, что элемент отображается на странице')
    def is_element_displaying(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIME_WAITER).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()
  
    @allure.step('Проверить, что элемент не отображается на странице')
    def is_element_not_displaying(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIME_WAITER).until(EC.invisibility_of_element_located(locator))
        return True

    @allure.step('Перетащить ингредиент в область заказа')
    def drag_and_drop(self, source_locator, target_locator):
        self.wait_and_find_element(source_locator)
        self.wait_and_find_element(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)
