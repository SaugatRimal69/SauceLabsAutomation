from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Option()
chrome_options.add_argument("--start-maximized")

service = Service("D:\Chromedriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options= chrome_options)

driver.get('https://sauce-demo.myshopify.com/account/login')

time.sleep(5)

UserName="//input[@id='customer_email']"
Password="//input[@id='customer_password']"

EC.visibility_of_element_located(UserName);

driver.find_element(By.XPATH, Username).clear()
driver.find_element(By.XPATH, Username).send_keys("ramshyam")



