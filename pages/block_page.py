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

    # метод отображения блока с выбором маршрута
    def get_text_type_mode_block(self):
        return self.get_text(BlockLocators.type_mode_block)

    # метод отображения текста сколько минут в пути
    def get_text_how_much_minute(self):
        return self.get_text(BlockLocators.how_much_minute_text)
    