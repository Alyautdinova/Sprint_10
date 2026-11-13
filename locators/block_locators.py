from selenium.webdriver.common.by import By

class BlockLocators:
    from_input = [By.ID, "from"]
    to_input = [By.ID, "to"]
    type_mode_block = [By.XPATH, "//div[@class='type-picker shown']//div[contains(@class,'mode')]"]
    how_much_minute_text = [By.XPATH, "//div[@class='results-text']"]
    active_type_mode_block = [By.XPATH, "//div[@class='type-picker shown']//div[contains(@class,'mode active')]"]
    active_type_transport = [By.XPATH, "//div[@class='types-container']/div[not(contains(@class, 'disabled'))]/img"]
    order_taxi_button = [By.XPATH, "//button[text()='Вызвать такси']"]
    order_drive_button = [By.XPATH, "//button[text()='Забронировать']"]

    # Оптимальный, Быстрый или Свой
    @staticmethod
    def type_mode_option(type_mode):
        return (By.XPATH, f"//div[@class='type-picker shown']//div[contains(@class,'mode')][text()='{type_mode}']")

    @staticmethod
    def type_transport_options_active_disabled(type_transport):
        return(By.XPATH, f"//div[@class='types-container']/div[contains(@class, 'active disabled')]/img[contains(@src,'{type_transport}')]")

    @staticmethod
    def type_transport_options_active(type_transport):
        return(By.XPATH, f"//img[contains(@src,'{type_transport}')]/parent::div[not(contains(@class, 'disabled'))]")
    