from selenium.webdriver.common.by import By

class TaxiOrderLocators:
    phone_input = [By.XPATH, "//div[text()='Телефон']"]
    payment_input = [By.XPATH, "//div[@class='pp-button filled']"]
    comment_input = [By.ID,"comment"]
    request_dropdown = [By.XPATH, "//div[@class='reqs-header']"]
    