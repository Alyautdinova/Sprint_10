from selenium.webdriver.common.by import By

class ModuleLocators:
    order_title = [By.XPATH, "//div[@class='order-header-title']"]
    time_element = [By.XPATH, "//div[@class='order-header-time']"]
    progress_element = [By.XPATH, "//div[contains(@class,'order-progress')]"]
    cancel_button = [By.XPATH, "//div[text()='Отменить']/preceding-sibling::button"]
    details_button = [By.XPATH, "//div[text()='Детали']/preceding-sibling::button"]
    more_about_trip_element = [By.XPATH, "//div[text()='Еще про поездку']/following-sibling::div"]
    raiting_icon = [By.XPATH, "//div[@class='order-button']/div[@class='order-btn-rating']"]
    taxist_img = [By.XPATH, "//div[@class='order-button']/img"]
    car_numer_element = [By.XPATH, "//div[@class='order-number']/div[@class='number']"]
    car_img = [By.XPATH, "//div[@class='order-number']/img"]
    