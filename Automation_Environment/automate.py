'''This is to automate writeups in a web browser/web page'''
import time
from selenium import webdriver # This is a framework and libraries for automating an application, most especially web browsers.
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome() # This is a variable object that carries a class of instanties
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
 
# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
popup.click()
 
 
 
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
 
time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()
 
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text



'''This phase allow the user to see a web opened for browsing'''

import time # Period in which the code run

from selenium import webdriver # This is lib that allow us to move through web with code

from selenium.webdriver.common.by import By # This point to fetch out an element

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element(By.CLASS_NAME, 'btn-default')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 
service = Service(executable_path='./chromedriver.exe')
 
chrome_browser = webdriver.Chrome(service=service)

'''Takes the user to automate web browswer just like how human interate with a browser'''
import time # This keeps the browser opening
from selenium import webdriver # This make it possible to use code to navigate and test the browser
from selenium.webdriver.common.by import By # This method allow selector into the browser body page
chrome_driver = webdriver.Chrome()  # This is brower object driver

chrome_driver.maximize_window() # This increases the browser font size

chrome_driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html') # This allows access to the specific browser url

assert 'Selenium Easy Demo' in chrome_driver.title # instead of using print use assert to check if the object really exist

show_message_button = chrome_driver.find_element(By.CLASS_NAME, 'btn-primary') 
# print(show_message_button.get_attribute('innerHTML'))

assert "Show Message" in chrome_driver.page_source
time.sleep(5)
user_message = chrome_driver.find_element(By.ID, "user-message")
user_button2 = chrome_driver.find_element(By.CSS_SELECTOR, '#get-input > .btn')
print(user_button2)
user_message.clear()
word_txt = "Programming isn't just about writing lines of codes but all about solving problems"
user_message.send_keys(word_txt)
show_message_button.click()
time.sleep(10)
output_message = chrome_driver.find_element(By.ID, "display")
print(word_txt in output_message.text)

#________ ALL THIS MAKE AUTOMATING A BROWSER POSSIBLE WITH THE HELP OF HUMAN ROBOT CALLED ------ SELENIUM