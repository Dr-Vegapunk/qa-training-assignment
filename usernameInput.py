from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")


driver.find_element(By.ID, "login-button").click()

try:
    wrongInput_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )
    print("Error message text:", wrongInput_error.text)
except:
    print("Error message not found!")

time.sleep(3)

driver.quit()