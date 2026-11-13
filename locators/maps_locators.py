from selenium.webdriver.common.by import By

class MapsLocators:
    route_pin = [By.XPATH, "//ymaps[contains(@class, 'route-pin__text')]/ymaps/ymaps"]