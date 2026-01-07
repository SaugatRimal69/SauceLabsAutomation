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

driver.get('https://sauce-demo.myshopify.com/account/login')

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


# SignUp= "//div[@class='seven columns offset-by-one desktop']//a[@id='customer_register_link']"
# click_element(driver, SignUp)
# print("SignUp is Clicker")


#Wait for navigation to registration page
time.sleep(2)

#Verify registration page opens properly by checking the URL
# if "register" in driver.current_url:
#     print("Registration gotm loaded successfully")
# else:
#     print("Warning: Registration form may not have loaded properly", driver.current_url)

#
# FirstName = "//input[@id='first_name']"
# send_keys_to_element(driver, FirstName, "Saugat")
# print("First Name entered")
#
#
#
#
# LastName= "//input[@id='last_name']"
# send_keys_to_element(driver, LastName, "Rimal")
# print("Last Name entered")
#
# EmailAddress = "//input[@id='email']"
#
# Email = f"testuser_{int(time.time())}@gmail.com" #f vaneko formatted string
# send_keys_to_element(driver, EmailAddress, Email)
# print("Email entered", Email)
#
#
# Password= "//input[@id='password']"
# send_keys_to_element(driver, Password, "abc")
# print("Password Entered")
#
# Create = "//input[@value='Create']"
# click_element(driver, Create)
# print("Create Vayo")

#Verify registration page opens properly by checking the URL
if "login" in driver.current_url:
    print("Login got loaded successfully")
else:
    print("Warning: Login form may not have loaded properly", driver.current_url)
time.sleep(5)

Email= "//input[@id='customer_email']"
send_keys_to_element(driver, Email, "testuser_1767783652@gmail.com")
print("Email is entered")

time.sleep(5)

Password = "//input[@id='customer_password']"
send_keys_to_element(driver, Password, "abc")
print("Password haliyo")

time.sleep(5)

SignIn = "//input[@value='Sign In']"
click_element(driver, SignIn)
print("Click vayo")

time.sleep(5)