from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys #In order to do something like press enter, arrow keys or anything where we can't type
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com") #Opens a page or a website

search_bar = driver.find_element(By.CLASS_NAME, "gLFyf") #This allows you to get the element you're working, this example we chose the class identifier for the search bar on google
search_bar.send_keys("Moo dang" + Keys.ENTER) #This allows you to type into the element

time.sleep(10)

driver.quit()

