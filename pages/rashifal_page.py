from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RashifalPage:
    # Locator for Tula Rashi
    TULA_RASHI = (By.XPATH, "//h3[contains(text(), 'तुला')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_tula_rashi_visible(self):
        # Check if Tula rashi is visible on the Rashifal page
        tula = self.wait.until(EC.visibility_of_element_located(self.TULA_RASHI))
        return tula.is_displayed()
