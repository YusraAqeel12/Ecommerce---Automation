import time
import random

from select import select
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://tutorialsninja.com/demo/")
browser.maximize_window()

#Select two iphones and take a screen shot
phones = browser.find_element(By.XPATH , ' //a[text()="Phones & PDAs"] ')
phones.click()
time.sleep(5)

HTV = browser.find_element(By.XPATH , '//a[text()="HTC Touch HD"]')
HTV.click()
time.sleep(5)

#unordered list mai kaafi list hain toh humnai class use kiya
Pics = browser.find_element(By.XPATH , '//ul[@class="thumbnails"]/li[1]')
Pics.click()
time.sleep(2)

arrow = browser.find_element(By.XPATH ,'//button[@title="Next (Right arrow key)"]')
for i in range(0,5):
    arrow.click()
    time.sleep(2)
#arrow.click
#arrow.click
#arrow.click
#arrow.click
#arrow.click

#arrow ko 5 baar click karanai kai bajay hum ismai range laga daingay

#screenshot liya hai and provide with name
browser.save_screenshot("screenshot" + str(random.randint(0,99)) + ".png")

Xbutton = browser.find_element(By.XPATH , '//button[@title="Close (Esc)"]')
Xbutton.click()
time.sleep(5)

qty = browser.find_element(By.ID , "input-quantity")
qty.click()
time.sleep(1)
qty.clear()
time.sleep(1)
qty.send_keys('5')
time.sleep(1)

addcart = browser.find_element(By.ID , 'button-cart')
addcart.click()
time.sleep(1)

addingcart = browser.find_element(By.XPATH , '//button[@class="btn btn-inverse btn-block btn-lg dropdown-toggle"] ')
addingcart.click()
time.sleep(1)

#Action chains is a way to automate low level interactions such as mouse movement , mouse button , keypress
#action aik varaible hai jismai actionchain class hai move karo element ko laptop var mai jismai hamara element ka path hai
laptop = browser.find_element(By.XPATH , '//a[text()="Laptops & Notebooks"]')
action = ActionChains(browser)
action.move_to_element(laptop).perform()

laptop5= browser.find_element(By.XPATH , '//a[text()="Show AllLaptops & Notebooks"]')
laptop5.click()
time.sleep(5)

ClickLaptop = browser.find_element(By.XPATH , ' //a[text()="HP LP3065"]')
ClickLaptop.click()

# Scroll to quantity of laptop , selenium will try to find this element and scroll to it
qtylaptop = browser.find_element(By.ID , 'input-quantity')
qtylaptop.location_once_scrolled_into_view
time.sleep(5)

laptopsendkey = browser.find_element(By.ID , 'input-quantity')
laptopsendkey.clear()
laptopsendkey.send_keys(5)
addtocart = browser.find_element(By.ID, 'button-cart')
addtocart.click()
time.sleep(5)

cartsec = browser.find_element(By.XPATH ,'//a[@title = "Checkout"]' )
cartsec.click()
time.sleep(5)

Guest = browser.find_element(By.XPATH , ' //input[@value="guest"] ')
Guest.click()
time.sleep(5)

Continue = browser.find_element(By.XPATH , '//input[@value="Continue"]')
Continue.click()

FirstName=browser.find_element(By.XPATH , '//input[@name="firstname"]')
FirstName.send_keys("Yusra")

LastName=browser.find_element(By.XPATH , '//input[@name="lastname"]')
LastName.send_keys("Aqeel")

email=browser.find_element(By.XPATH , '//input[@name="email"]')
email.send_keys("yusraaqeel12@gmail.com")

phonenumber=browser.find_element(By.XPATH , '//input[@name="telephone"]')
phonenumber.send_keys("7887878798")

address=browser.find_element(By.XPATH , '//input[@name="address_2"]')
address.send_keys("karim apartment ")

city=browser.find_element(By.XPATH , '//input[@name="city"]')
city.send_keys("karachi")

postcode=browser.find_element(By.XPATH , '//input[@name="postcode"]')
postcode.send_keys("8978")

#Dropdown mai select kai liyae we have three different approches
country = browser.find_element(By.ID , "input-payment-country")
dropdown=Select(country)
dropdown.select_by_value("21")

countryzone = browser.find_element(By.ID , "input-payment-zone")
dropdown=Select(countryzone)
dropdown.select_by_visible_text("Antwerpen")

buttonSecond= browser.find_element(By.ID , 'button-guest')
buttonSecond.click()

checkbox=browser.find_element(By.XPATH , '//input[@name ="agree"]')
checkbox.click()

buttonthird=browser.find_element(By.XPATH ,'//input[@value ="Continue"] ')
buttonthird.click()