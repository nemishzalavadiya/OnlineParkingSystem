from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


user_name = "kevaltalaviya007@gmail.com"
password = "keval1"
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/login/?role=User")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(1)
user_name = "kevaltalaviya007@gmail.com"
password = "keval"	
driver.get("http://127.0.0.1:8000/login/?role=User")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/a').click()
time.sleep(3)


user_name = "kevaltalaviya007@gmail.com"
password = "keval12"
driver.get("http://127.0.0.1:8000/login/?role=Landlord")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(1)
user_name = "keval@gmail.com"
password = "keval123"
driver.get("http://127.0.0.1:8000/login/?role=Landlord")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/a').click()
time.sleep(3)

user_name = "kevaltalaviya007@gmail.com"
password = "keval1"
driver.get("http://127.0.0.1:8000/login/?role=Admin")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/button').click()
time.sleep(1)
user_name = "kevalkeval@gmail.com"
password = "keval"
driver.get("http://127.0.0.1:8000/login/?role=Admin")
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input")
element.send_keys(user_name)
element = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
element.send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/a').click()
time.sleep(3)

element.send_keys(Keys.RETURN)
