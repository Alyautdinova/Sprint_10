from selenium.webdriver.common.by import By

class TariffLocators:
    tariff_card = [By.XPATH, "//div[@class='tariff-cards']/div[contains(@class,'tcard')]"]
    active_tariff_card_title = [By.XPATH, "//div[@class='tariff-cards']/div[contains(@class,'tcard active')]/div[@class='tcard-title']"]
    information_button = [By.XPATH, "//button[contains(@class,'i-button')]"]

    @staticmethod
    def tariff(tariff_name):
        return (By.XPATH, f"//div[@class='tcard-title'][text()='{tariff_name}']")
    
    @staticmethod
    def icon_tariff(tariff_name):
        return (By.XPATH, f"//div[text()='{tariff_name}']/parent::div/button")

    @staticmethod
    def describe_tariff(tariff_name):
        return (By.XPATH, f"//div[contains(@class,'i-floating')]/div[text()='{tariff_name}']/following-sibling::div[@class='i-dPrefix']")