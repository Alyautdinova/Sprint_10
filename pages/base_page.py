from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # метод поиска всех элементов с ожиданием
    def find(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    # метод поиска всех элементов с ожиданием
    def find_all(self, locator):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(locator))

    # скролл до элемента
    def scroll_to(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # метод ввода текста в поле с ожиданием
    def send_keys(self, locator, text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    # метод нажатия на элемент с ожидаем кликабельности
    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    # JS клик на элемент с ожидаем кликабельности
    def js_click(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    # метод получения текстового значения
    def get_text(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    # метод получения текстовых значений
    def get_texts(self, locator):
        elements = self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))
        texts = []
        for element in elements:
            texts.append(element.text)
        return texts

    # метод открытия страницы
    def open(self, url):
        self.driver.get(url)

    # метод получения текущего урла
    def get_current_url(self):
        return self.driver.current_url

    # метод наведения на элемент
    def hover(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        #self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    # метод проверки исчезновения элемента
    def wait_element_disappear(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))