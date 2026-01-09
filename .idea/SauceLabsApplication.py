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
    element.send_keys(keys)

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
time.sleep(2)



login_search_data = [
    {
        "email": "rasputrump911@gmail.com",
        "password": "abcdefgh",
        "search_term": "Grey Jacket",
        "path":"//h3[normalize-space()='Grey jacket']"
    },

    {
        "email": "jay123@gmail.com",
        "password": "abcdefgh",
        "search_term": "Black heels",
        "path":"//h3[normalize-space()='Black heels']"

    },
    {
        "email": "jay1234@gmail.com",
        "password": "abcdefgh",
        "search_term": "Brown Shades",
        "path":"//h3[normalize-space()='Brown Shades']"
    }


]


login_search_data2 = [
    {
        # "email": "rasputrump911@gmail.com",
        # "password": "abcdefgh",
        "search_term": "Grey Jacket",
        "path":"//h3[normalize-space()='Grey jacket']"
    },

    {
        # "email": "jay123@gmail.com",
        # "password": "abcdefgh",
        "search_term": "Black heels",
        "path":"//h3[normalize-space()='Black heels']"

    },
    {
        # "email": "jay1234@gmail.com",
        # "password": "abcdefgh",
        "search_term": "Brown Shades",
        "path":"//h3[normalize-space()='Brown Shades']"
    }


]

#
# for i, user_data in enumerate(login_search_data):
#     driver.get('https://sauce-demo.myshopify.com/')
#
#
#
# login_link="//a[@id='customer_login_link']"
# click_element(driver,login_link)
# print("Clicked on Log In Link")
#
#
#
#
# Email= "//input[@id='customer_email']"
# send_keys_to_element(driver, Email, user_data["email"])
# print(f"Email entered: {user_data['email']}")
#
# time.sleep(2)
#
# Password = "//input[@id='customer_password']"
# send_keys_to_element(driver, Password, user_data["password"])
# print(f"Password entered: {user_data['password']}")
#
# time.sleep(2)
#
# SignIn = "//input[@value='Sign In']"
# click_element(driver, SignIn)
# print("Click vayo")
#
# time.sleep(30)
#

# GreyJacket="//img[@alt='Grey jacket']"
# BrownShades="//img[@alt='Bronze sandals']"
# BlackHeels="//img[@alt='Black heels']"
SearchButton = "//input[@id='search-field']"
checkout="//a[normalize-space()='Check Out']"
greypath="//h3[normalize-space()='Grey jacket']"
SearchButton2 = "//input[@id='search-submit']"
addtocart="//input[@id='add']"
# for i, user_data in enumerate(login_search_data):
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
    click_element(driver,user_data['path'])
    time.sleep(2)
    click_element(driver,addtocart)
    time.sleep(2)
    click_element(driver,checkout)






    # print("Search click vayo")
    # click_element(driver, user_data['path'])
    # print("Link ni click vayo")
    time.sleep(2)





