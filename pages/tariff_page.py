from pages.base_page import BasePage
from locators.tariff_locators import TariffLocators

class TariffPage(BasePage):
        
    # метод отображения блоков тарифов
    def is_visible_tariff_card(self):
        return self.find_all(TariffLocators.tariff_card)

    # метод отображения активного тарифа
    def is_visible_active_tariff_card(self):
        return self.find_all(TariffLocators.active_tariff_card_title)

    # метод отображения активного тарифа
    def is_visible_active_tariff_card_title(self):
        return self.get_text(TariffLocators.active_tariff_card_title)

    # метод нажатия на тариф
    def click_tariff(self, tariff_name):
        self.click(TariffLocators.tariff(tariff_name))

    # метод нажатия на иконку i тарифа
    def click_icon_tariff(self, tariff_name):
        self.hover(TariffLocators.icon_tariff(tariff_name))

    # метод отображения описания тарифа
    def get_describe_tariff(self, tariff_name):
        return self.get_text(TariffLocators.describe_tariff(tariff_name))
