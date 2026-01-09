from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time




chrome_options = Options()
chrome_options.add_argument("--start-maximized")

#location of chromedriver

service = Service(r"D:\Chromedriver\chromedriver-win64\chromedriver.exe")

#initialize the driver

driver = webdriver.Chrome(service=service, options= chrome_options)

driver.get('https://sauce-demo.myshopify.com')

time.sleep(5)

# UserName="//input[@id='customer_email']"
# Password="//input[@id='customer_password']"
#
# EC.visibility_of_element_located(UserName);
#
# driver.find_element(By.XPATH, UserName).clear()
# driver.find_element(By.XPATH, UserName).send_keys("ramshyam")



def click_element(driver,xpath):
    element= driver.find_element(By.XPATH,xpath)
    element.click()

def send_keys_to_element(driver,xpath,keys):
    element = driver.find_element(By.XPATH,xpath)
    element.clear()
    element.send_keys()

def clear(driver,xpath):
    element= driver.find_element(By.XPATH,xpath)
    element.clear()



time.sleep(2)




GrayJacket = "//h3[normalize-space()='Grey jacket']"
click_element(driver, GrayJacket)
print("Gray jacket was selected")

time.sleep(2)

if "gray-jacket" in driver.current_url:
    print("Gray jacket kinna pugiyo")
else:
    print("Kinna pugiyena", driver.current_url)

AddToCart = "//input[@id='add']"
click_element(driver, AddToCart)
print("Cart ma gayo")

time.sleep(2)


driver.refresh()

time.sleep(5)

MyCart = "//a[@class='toggle-drawer cart desktop ']"
click_element(driver, MyCart)
print("my cart click vayo")





time.sleep(5)
CheckOut = "//input[@value='Check Out']"
clear(driver, CheckOut)
print ("CheckOut Vayo")
time.sleep(2)