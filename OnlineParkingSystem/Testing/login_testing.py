from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


user_name = "user31@gmail.com"
password = "12345678"
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/login/?role=User")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(1)

user_name = "user1@gmail.com"
password = "12345678"
driver.get("http://127.0.0.1:8000/login/?role=User")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/a').click()
time.sleep(3)


user_name = "landlord1@gmail.com"
password = "12345678"
driver.get("http://127.0.0.1:8000/login/?role=Landlord")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/a').click()
time.sleep(1)

user_name = "landl1@gmail.com"
password = "12345678"
driver.get("http://127.0.0.1:8000/login/?role=Landlord")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(3)

user_name = "ad@gmail.com"
password = "12345678"
driver.get("http://127.0.0.1:8000/login/?role=Admin")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(1)

user_name = "nemish@gmail.com"
password = "123"
driver.get("http://127.0.0.1:8000/login/?role=Admin")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(3)

user_name="Nemish"
email="13101999nemish@gmail.com"
mobile="9876543214"
age="18"
driver.get("http://127.0.0.1:8000/registration/?role=Landlord")
element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[1]/input")
element.send_keys(user_name)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[2]/input")
element.send_keys(email)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[3]/input")
element.send_keys(mobile)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[4]/input")
element.send_keys(age)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[5]/input")
element.send_keys("12345")

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[6]/input")
element.send_keys("12345")
time.sleep(1)
#driver.find_element_by_xpath("").click()
box=driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[7]/div/input")

time.sleep(3)
driver.execute_script("arguments[0].click();",box)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[8]/div/button').click()

time.sleep(6)


user_name="Nemish"
email="13nemish@gmail.com"
mobile="9873543214"
age="25"
driver.get("http://127.0.0.1:8000/registration/?role=Landlord")
element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[1]/input")
element.send_keys(user_name)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[2]/input")
element.send_keys(email)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[3]/input")
element.send_keys(mobile)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[4]/input")
element.send_keys(age)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[5]/input")
element.send_keys("12345678")

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[6]/input")
element.send_keys("12345678")
time.sleep(1)
#driver.find_element_by_xpath("").click()
box=driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[7]/div/input")

driver.execute_script("arguments[0].click();",box)

element.send_keys(Keys.RETURN)
