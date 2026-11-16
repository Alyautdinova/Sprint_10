import allure
import pytest
import re

from pages.block_page import BlockPage
from pages.tariff_page import TariffPage
from pages.taxi_orders_page import TaxiOrdersPage
from pages.module_page import ModulePage
from data.data_test import OPTIMAL_TYPE, FAST_TYPE, SELF_TYPE, CAR_TRANSPORT, TAXI_TRANSPORT, DRIVE_TRANSPORT, WORK_TARIFF, SLEEP_TARIFF, VACATION_TARIFF, TALK_TARIFF, COMFORTING_TARIFF, GLAMUR_TARIFF

class TestOrderTaxi:
    @allure.title('Переключение между Оптимальный и Быстрый')
    @allure.description('При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута')
    def test_choise_type_mode(self, create_default_route, driver):
        with allure.step('Проверка, что "Быстрый" стоит по умолчанию'):
            blockPage = BlockPage(driver)
            assert blockPage.get_text_active_type_mode_block() == FAST_TYPE

        with allure.step('Проверка стоимости маршрута и времени для опции "Быстрый/Такси"'):
            assert "Такси ~ X руб. В пути X мин." in blockPage.get_text_how_much_minute_with_regex()
            assert blockPage.is_visible_type_transport_options_active_disabled(TAXI_TRANSPORT)

        with allure.step('Нажатие на опцию "Оптимальный"'):
            blockPage.click_type_mode_block(OPTIMAL_TYPE)

        with allure.step('Проверка, что опция "Оптимальный" стала активной'):
            assert blockPage.get_text_active_type_mode_block() == OPTIMAL_TYPE

        with allure.step('Проверка стоимости маршрута и времени для опции "Оптимальный/Авто"'):
            assert "Авто ~ X руб. В пути X мин." in blockPage.get_text_how_much_minute_with_regex()
            assert blockPage.is_visible_type_transport_options_active_disabled(CAR_TRANSPORT)

    @allure.title('Отображение видов маршрута для типа Свой')
    @allure.description('При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)')
    def test_choise_self_type_mode(self, create_default_route, driver):
        with allure.step('Нажатие на опцию "Свой"'):
            blockPage = BlockPage(driver)
            blockPage.click_type_mode_block(SELF_TYPE)

        with allure.step('Проверка, что опция "Свой" стала активной'):
            assert blockPage.get_text_active_type_mode_block() == SELF_TYPE

        with allure.step('Проверка, что активные 6 типов передвижения'):
            assert len(blockPage.is_visible_active_type_transport()) == 6

    @allure.title('Отображение кнопки "Вызвать такси"')
    @allure.description('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_active_button_order_taxi(self, create_default_route, driver):
        with allure.step('Проверка, что отображается кнопка "Вызвать такси"'):
            blockPage = BlockPage(driver)
            assert blockPage.is_visible_order_taxi_button()

    @allure.title('Отображение кнопки "Забронировать"')
    @allure.description('При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_active_button_order_drive(self, create_default_route, driver):
        with allure.step('Нажатие на опцию "Свой" и "Драйв"'):
            blockPage = BlockPage(driver)
            blockPage.click_type_mode_block(SELF_TYPE)
            blockPage.click_active_type_transport()

        with allure.step('Проверка, что отображается кнопка "Забронировать"'):
            assert blockPage.is_visible_order_drive_button()

    @allure.title('Отображение тарифов')
    @allure.description('Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный')
    def test_open_taxi_order_form_with_tariffs(self, create_default_route, driver):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()

        with allure.step('Проверка, что отображается 6 тарифов и активный Рабочий'):
            tariffPage = TariffPage(driver)
            assert len(tariffPage.is_visible_tariff_card()) == 6
            assert len(tariffPage.is_visible_active_tariff_card()) == 1
            assert tariffPage.is_visible_active_tariff_card_title() == WORK_TARIFF

    @allure.title('Отображение описание тарифа')
    @allure.description('При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ')
    @pytest.mark.parametrize("tariff_name, expected_description", [
    (WORK_TARIFF, "Для деловых особ, которых отвлекают"),
    
    pytest.param(
        SLEEP_TARIFF, 
        "Для тех, кто не выспался", 
        marks=pytest.mark.xfail(reason="Баг: описание тарифа не соответствует ТЗ")
    ),
    
    (VACATION_TARIFF, "Если пришла пора отдохнуть"),
    
    pytest.param(
        TALK_TARIFF, 
        "Если мысли не выходят из головы", 
        marks=pytest.mark.xfail(reason="Баг: описание тарифа не соответствует ТЗ")
    ),
    
    (COMFORTING_TARIFF, "Если хочется свернуться калачиком"),
    (GLAMUR_TARIFF, "Если нужно блистать"),
    ])
    def test_tariff_tooltip(self, create_default_route, driver, tariff_name, expected_description):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()

        with allure.step(f'Наведение на иконку тарифа "{tariff_name}"'):
            tariffPage = TariffPage(driver)
            tariffPage.click_tariff(tariff_name)
            tariffPage.click_icon_tariff(tariff_name)
            
        with allure.step('Проверка текста описания'):
            assert expected_description in tariffPage.get_describe_tariff(tariff_name)

    @allure.title('Отображение элементов для заказа такси')
    @allure.description('Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу')
    def test_display_inputs(self, create_default_route, driver):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()

        with allure.step('Проверка, что отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу'):
            taxiOrdersPage = TaxiOrdersPage(driver)
            assert taxiOrdersPage.is_visible_block_for_order_taxi()

    @allure.title('Отображение окна "Поиск машины"')
    @allure.description('Появляется окно ожидания машины')
    def test_display_module_find_car(self, create_default_route, driver):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()

        with allure.step('Выбор столика для ноутбука и нажатие на кнопку "Ввести номер и заказать"'):
            taxiOrdersPage = TaxiOrdersPage(driver)
            taxiOrdersPage.click_request_dropdown()
            taxiOrdersPage.click_laptope_table_slider()
            taxiOrdersPage.click_order_taxi()

        with allure.step('Проверка, что отображается окно "Поиск машины"'):
            modulePage = ModulePage(driver)
            assert modulePage.get_order_title() == "Поиск машины"
            assert modulePage.is_visible_module_find_car()

    @allure.title('Отображение окна совершенного заказа')
    @allure.description('При дожидании окончания таймера поиска машины, отображается окно совершенного заказа')
    def test_display_module_ordered_taxi(self, create_default_route, driver):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()

        with allure.step('Нажатие на кнопку "Ввести номер и заказать"'):
            taxiOrdersPage = TaxiOrdersPage(driver)
            taxiOrdersPage.click_order_taxi()

        with allure.step('Проверка отображения окна совершенного заказа'):
            modulePage = ModulePage(driver)
            modulePage.is_not_visible_progress_element()
            modulePage.is_visible_module_ordered_taxi()

    @allure.title('Проверка стоимости поездки в блоке "Еще про поездку"')
    @allure.description('При нажатии на кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа')
    def test_price_in_more_about_trip(self, create_default_route, driver):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()
            price1 = int(re.search(r'\d+', blockPage.get_text_how_much_minute()).group())

        with allure.step('Нажатие на кнопку "Ввести номер и заказать"'):
            taxiOrdersPage = TaxiOrdersPage(driver)
            taxiOrdersPage.click_order_taxi()

        with allure.step('Нажатие на кнопку "Детали"'):
            modulePage = ModulePage(driver)
            modulePage.click_details_button()

        with allure.step('Проверка стоимости такси'):
            assert int(re.search(r'\d+', modulePage.get_text_more_about_trip_element()).group()) == price1

    @allure.title('Закрытие окна "Поиск машины" при нажатии на кнопку "Отмена"')
    @allure.description('При нажатии на кнопку Отмена окно закрывается')
    def test_сlose_module_find_car(self, create_default_route, driver):
        with allure.step('Нажатие на кнопку "Вызвать такси"'):
            blockPage = BlockPage (driver)
            blockPage.click_order_taxi_button()

        with allure.step('Нажатие на кнопку "Ввести номер и заказать"'):
            taxiOrdersPage = TaxiOrdersPage(driver)
            taxiOrdersPage.click_order_taxi()

        with allure.step('Нажатие на кнопку "Отмена"'):
            modulePage = ModulePage(driver)
            modulePage.click_cancel_button()

        with allure.step('Проверка, что окно "Поиск машины" закрыто'):
            assert modulePage.is_not_visible_module_find_car()
    