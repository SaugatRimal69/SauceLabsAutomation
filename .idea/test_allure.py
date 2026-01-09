from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure

# Helper functions for Allure steps
@allure.step("Click on element with xpath: {xpath}")
def click_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

@allure.step("Send keys '{keys}' on element with xpath: {xpath}")
def send_keys_to_element(driver, xpath, keys):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(keys)

# --- THE FIX: Wrap your entire logic in ONE test function ---
def test_sauce_demo_search():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # location of chromedriver
    service = Service(r"D:\Chromedriver\chromedriver-win64\chromedriver.exe")

    # initialize the driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get('https://sauce-demo.myshopify.com/account/login')
        time.sleep(5)

        login_search_data2 = [
            {"search_term": "Grey Jacket", "path": "//h3[normalize-space()='Grey jacket']"},
            {"search_term": "Black heels", "path": "//h3[normalize-space()='Black heels']"},
            {"search_term": "Brown Shades", "path": "//h3[normalize-space()='Brown Shades']"}
        ]

        SearchButton = "//input[@id='search-field']"
        checkout = "//a[normalize-space()='Check Out']"
        SearchButton2 = "//input[@id='search-submit']"
        addtocart = "//input[@id='add']"

        for i, user_data in enumerate(login_search_data2):
            driver.get('https://sauce-demo.myshopify.com/')

            click_element(driver, SearchButton)
            print("Search click vayo")
            time.sleep(2)

            send_keys_to_element(driver, SearchButton, user_data['search_term'])
            print(f"Search vako kura {user_data['search_term']}")
            time.sleep(2)

            click_element(driver, SearchButton2)
            time.sleep(2)

            click_element(driver, user_data['path'])
            time.sleep(2)

            click_element(driver, addtocart)
            time.sleep(2)

            click_element(driver, checkout)
            print("Link ni click vayo")
            time.sleep(2)

    finally:
        driver.quit()