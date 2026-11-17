from pages.base_page import BasePage
from locators.taxi_order_locators import TaxiOrderLocators

class TaxiOrdersPage(BasePage):
    
    # метод отображения поля "Телефон"
    def is_visible_phone_input(self):
        return self.find(TaxiOrderLocators.phone_input).is_displayed()

    # метод отображения поля "Способ оплаты"
    def is_visible_payment_input(self):
        return self.find(TaxiOrderLocators.payment_input).is_displayed()

    # метод отображения поля "Комментарий водителю"
    def is_visible_comment_input(self):
        return self.find(TaxiOrderLocators.comment_input).is_displayed()

    # метод отображения поля "Требования к заказу"
    def is_visible_request_dropdown(self):
        return self.find(TaxiOrderLocators.request_dropdown).is_displayed()

    # метод нажатие на поле "Требования к заказу"
    def click_request_dropdown(self):
        self.click(TaxiOrderLocators.request_dropdown)

    # метод нажатия на "Столик для ноутбука"
    def click_laptope_table_slider(self):
        self.click(TaxiOrderLocators.laptope_table_slider)

    # метод нажатия на "Ввести номер и заказать"
    def click_order_taxi(self):
        self.js_click(TaxiOrderLocators.order_taxi)

    # метод отображения блока для заказа такси
    def is_visible_block_for_order_taxi(self):
        results = [
            self.is_visible_phone_input(),
            self.is_visible_payment_input(),
            self.is_visible_comment_input(),
            self.is_visible_request_dropdown()
        ]
        return all(results)
    