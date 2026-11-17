from pages.base_page import BasePage
from locators.maps_locators import MapsLocators

class MapsPage(BasePage):

    # метод для возвращения текста пинов
    def get_route_text(self):
        return self.get_texts(MapsLocators.route_pin)
