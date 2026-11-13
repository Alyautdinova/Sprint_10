from selenium.webdriver.common.by import By

class BlockLocators:
    from_input = [By.ID, "from"]
    to_input = [By.ID, "to"]
    type_mode_block = [By.XPATH, "//div[@class='type-picker shown']//div[contains(@class,'mode')]"]
    how_much_minute_text = [By.XPATH, "//div[@class='results-text']"]
    