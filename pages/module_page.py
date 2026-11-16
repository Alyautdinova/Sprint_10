from pages.base_page import BasePage
from locators.module_locators import ModuleLocators

class ModulePage(BasePage):

    # метод проверки заголовка окна
    def get_order_title(self):
        return self.get_text(ModuleLocators.order_title)

    # метод проверки, что окно "Поиск машины" не отображается
    def is_not_visible_module_find_car(self):
        return self.wait_element_disappear(ModuleLocators.progress_element)

    # метод отображения времени поиска машины
    def is_visible_time_element(self):
        return self.find(ModuleLocators.time_element).is_displayed()

    # метод отображения таймера обратного отсчета
    def is_visible_progress_element(self):
        return self.find(ModuleLocators.progress_element).is_displayed()

    # метод проверки, что таймера обратного отсчета не отображается
    def is_not_visible_progress_element(self):
        return self.wait_element_disappear(ModuleLocators.progress_element)

    # метод отображения кнопки "Отменить"
    def is_visible_cancel_button(self):
        return self.find(ModuleLocators.cancel_button).is_displayed()

    # метод отображения кнопки "Детали"
    def is_visible_details_button(self):
        return self.find(ModuleLocators.details_button).is_displayed()

    # метод отображения окна "Поиск машины"
    def is_visible_module_find_car(self):
        results = [
            self.is_visible_time_element(),
            self.is_visible_progress_element(),
            self.is_visible_cancel_button(),
            self.is_visible_details_button()
        ]
        return all(results)

    # метод нажатия на кнопку "Отменить"
    def click_cancel_button(self):
        self.click(ModuleLocators.cancel_button)

    # метод нажатия на кнопку "Детали"
    def click_details_button(self):
        self.click(ModuleLocators.details_button)

    # метод отображения блока "Еще про поездку"
    def get_text_more_about_trip_element(self):
        return self.get_text(ModuleLocators.more_about_trip_element)

    # метод отображения иконки рейтинга
    def is_visible_raiting_icon(self):
        return self.find(ModuleLocators.raiting_icon).is_displayed()

    # метод отображения аватарки таксиста
    def is_visible_taxist_img(self):
        return self.find(ModuleLocators.taxist_img).is_displayed()

    # метод отображения номера машины
    def is_visible_car_numer_element(self):
        return self.find(ModuleLocators.car_numer_element).is_displayed()

    # метод отображения картинки машины
    def is_visible_pcar_img(self):
        return self.find(ModuleLocators.car_img).is_displayed()

    # метод отображения совершенного заказа Такси
    def is_visible_module_ordered_taxi(self):
        results = [
            self.is_visible_raiting_icon(),
            self.is_visible_taxist_img(),
            self.is_visible_car_numer_element(),
            self.is_visible_pcar_img(),
            self.is_visible_cancel_button(),
            self.is_visible_details_button()
        ]
        return all(results)
    