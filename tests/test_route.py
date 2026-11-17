import allure

from pages.maps_page import MapsPage
from pages.block_page import BlockPage
from data.urls import Urls
from data.data_test import FROM_ADDRESS, TO_ADDRESS, OPTIMAL_TYPE, FAST_TYPE, SELF_TYPE

class TestRoute:

    @allure.title('Отрисовка маршрута')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" на карте отображаются две точки начала и конца маршрута')
    def test_create_route_with_unique(self, create_default_route, driver):
        with allure.step('Проверка, что 2 точки на карте'):
            mapsPage = MapsPage(driver)
            assert len(mapsPage.get_route_text()) == 2
        with allure.step('Проверка, что отображается адрес откуда и куда'):
            # склеиваем список в одну строку через пробел
            route_text = " ".join(mapsPage.get_route_text())
            assert FROM_ADDRESS in route_text
            assert TO_ADDRESS in route_text

    @allure.title('Отрисовка блока с выбором маршрута с разными адресами')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута')
    def test_route_block_appears_different_addresses(self, create_default_route, driver):
        with allure.step('Проверка отображения блока с выбором маршрута'):
            blockPage = BlockPage(driver)
            assert OPTIMAL_TYPE in blockPage.get_text_type_mode_block()
            assert FAST_TYPE in blockPage.get_text_type_mode_block()
            assert SELF_TYPE in blockPage.get_text_type_mode_block()

    @allure.title('Отрисовка блока с выбором маршрута с одинаковыми адресами')
    @allure.description('При вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."')
    def test_route_block_same_addresses(self, driver):
        with allure.step('Открытие главной страницы'):
            blockPage = BlockPage(driver)
            blockPage.open(Urls.BASE_URL)
        with allure.step('Ввод одинакового адреса в откуда и куда'):
            blockPage.set_address(FROM_ADDRESS, FROM_ADDRESS)
        with allure.step('Проверка отображения текста "Авто Бесплатно В пути 0 мин."'):
            assert blockPage.get_text_how_much_minute() == "Авто Бесплатно В пути 0 мин."
    