from pages.base_page import BasePage
from locators.taxi_order_locators import TaxiOrderLocators

class TaxiOrdersPage(BasePage):
    
    # метод отображения поля Телефон
    def is_visible_phone_input(self):
        return self.find(TaxiOrderLocators.phone_input).is_displayed()

    # метод отображения поля Способ оплаты
    def is_visible_payment_input(self):
        return self.find(TaxiOrderLocators.payment_input).is_displayed()

    # метод отображения поля Комментарий водителю
    def is_visible_comment_input(self):
        return self.find(TaxiOrderLocators.comment_input).is_displayed()

    # метод отображения поля Требования к заказу
    def is_visible_request_dropdown(self):
        return self.find(TaxiOrderLocators.request_dropdown).is_displayed()
    