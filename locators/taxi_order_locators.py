from selenium.webdriver.common.by import By

class TaxiOrderLocators:
    phone_input = [By.XPATH, "//div[text()='Телефон']"]
    payment_input = [By.XPATH, "//div[@class='pp-button filled']"]
    comment_input = [By.ID,"comment"]
    request_dropdown = [By.XPATH, "//div[@class='reqs-header']"]
    laptope_table_slider = [By.XPATH, "//div[text()='Столик для ноутбука']/following-sibling::div//span"]
    order_taxi = [By.XPATH, "//button[@class='smart-button']"]
