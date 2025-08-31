import pytest
from selenium import webdriver
from home_page import HomePage
from rashifal_page import RashifalPage
import time


@pytest.fixture
def driver():
    # Setup: Initialize browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: Quit browser
    time.sleep(2)
    driver.quit()


def test_tula_rashi_visible(driver):
    home = HomePage(driver)
    rashifal = RashifalPage(driver)

    # Step 1: Open homepage
    home.open()

    # Step 2: Navigate to Rashifal
    home.click_rashifal()
    
    time.sleep(2)  # Wait for page to load

    # Step 3: Verify Tula rashi is visible
    assert rashifal.is_tula_rashi_visible(), "❌ Tula Rashi is not visible!"
    print("✅ Tula Rashi is visible on Rashifal page.")
