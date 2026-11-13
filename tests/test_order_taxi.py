import allure

from pages.block_page import BlockPage
from data.data_test import OPTIMAL_TYPE, FAST_TYPE, SELF_TYPE, CAR_TRANSPORT, TAXI_TRANSPORT, DRIVE_TRANSPORT

class TestOrderTaxi:
    @allure.title('Подготовка к заказу такси')
    @allure.description('При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута')
    def test_choise_type_mode(self, create_default_route, driver):
        blockPage = BlockPage(driver)
        assert blockPage.get_text_active_type_mode_block() == FAST_TYPE

        assert "Такси ~ 194 руб. В пути 4 мин." in blockPage.get_text_how_much_minute()

        assert blockPage.is_visible_type_transport_options_active_disabled(TAXI_TRANSPORT)

        blockPage.click_type_mode_block(OPTIMAL_TYPE)
        assert blockPage.get_text_active_type_mode_block() == OPTIMAL_TYPE

        assert "Авто ~ 40 руб. В пути 5 мин." in blockPage.get_text_how_much_minute()

        assert blockPage.is_visible_type_transport_options_active_disabled(CAR_TRANSPORT)

    @allure.title('Подготовка к заказу такси')
    @allure.description('При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)')
    def test_choise_self_type_mode(self, create_default_route, driver):
        blockPage = BlockPage(driver)
        blockPage.click_type_mode_block(SELF_TYPE)

        assert blockPage.get_text_active_type_mode_block() == SELF_TYPE

        assert len(blockPage.is_visible_active_type_transport()) == 6

    @allure.title('Подготовка к заказу такси')
    @allure.description('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_active_button_order_taxi(self, create_default_route, driver):
        blockPage = BlockPage(driver)
        assert blockPage.is_visible_order_taxi_button()

    @allure.title('Подготовка к заказу такси')
    @allure.description('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_active_button_order_drive(self, create_default_route, driver):
        blockPage = BlockPage(driver)
        blockPage.click_type_mode_block(SELF_TYPE)
        blockPage.click_active_type_transport(DRIVE_TRANSPORT)

        assert blockPage.is_visible_order_drive_button()