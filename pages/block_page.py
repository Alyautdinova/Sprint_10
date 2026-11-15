import re

from pages.base_page import BasePage
from locators.block_locators import BlockLocators

class BlockPage(BasePage):

    # метод заполнения поля "Откуда"
    def set_from_address(self, from_address):
        self.send_keys(BlockLocators.from_input, from_address)

    # метод заполнения поля "Куда"
    def set_to_address(self, to_address):
        self.send_keys(BlockLocators.to_input, to_address)

    # метод заполнения адреса
    def set_address(self, from_address, to_address):
        self.set_from_address(from_address)
        self.set_to_address(to_address)

    # метод отображения текста для блока с выбором маршрута
    def get_text_type_mode_block(self):
        return self.get_text(BlockLocators.type_mode_block)

    # метод отображения текста сколько минут в пути
    def get_text_how_much_minute(self):
        return re.sub(r'\d+', 'X', self.get_text(BlockLocators.how_much_minute_text).replace("\n", " "))

    # метод отображения текста для активного блока с выбором маршрута
    def get_text_active_type_mode_block(self):
        return self.get_text(BlockLocators.active_type_mode_block)

    # метод выбора вида маршрута (Оптимальный, Быстрый или Свой)
    def click_type_mode_block(self, type_mode):
        self.click(BlockLocators.type_mode_option(type_mode))

    # метод отображения активного единственного вида транспорта (без возможности выбора)
    def is_visible_type_transport_options_active_disabled(self, type_transport):
        return self.find(BlockLocators.type_transport_options_active_disabled(type_transport)).is_displayed()

    # метод отображения активных видов транспорта (с возможностью выбора)
    def is_visible_active_type_transport(self):
        return self.find_all(BlockLocators.active_type_transport)

    # метод выбора средства передвижения
    def click_active_type_transport(self):
        self.move_to_element(BlockLocators.drive_type)
    
    # метод отображения кнопки "Вызвать такси"
    def is_visible_order_taxi_button(self):
        return self.find(BlockLocators.order_taxi_button).is_displayed()

    # метод отображения кнопки "Вызвать такси"
    def click_order_taxi_button(self):
        self.click(BlockLocators.order_taxi_button)
    
    # метод отображения кнопки "Забронировать"
    def is_visible_order_drive_button(self):
        return self.find(BlockLocators.order_drive_button).is_displayed()
    
    # метод отображения кнопки "Забронировать"
    def click_order_drive_button(self):
        self.click(BlockLocators.order_drive_button)