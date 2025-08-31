from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    # Locators
    RASHIFAL_LINK = (By.LINK_TEXT, "Rashifal")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
    # Open HamroPatro homepage
        self.driver.get("https://www.hamropatro.com/")

    def click_rashifal(self):
        # Click on the Rashifal tab
        rashifal = self.wait.until(EC.element_to_be_clickable(self.RASHIFAL_LINK))
        rashifal.click()
