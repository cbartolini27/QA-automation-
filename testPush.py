from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys #In order to do something like press enter, arrow keys or anything where we can't type
from selenium.webdriver.support.ui import WebDriverWait #Allow for us to wait on the presence of an element before we move forward. Page might take time to load and during that time we might access an element that doesnt exist
from selenium.webdriver.support import expected_conditions as EC #Allow for us to wait on the presenece of an element before we move forward
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com") #Opens a page or a website

"""
Uses our web driver, wait for up to 5 seconds until we locate an element by its class name that has the "gLFyf" identifier. 
Want to put this before input element. Now if you were to have a slow internet connection it will wait 5 seconds to find the
element before terminating the program
"""
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

search_bar = driver.find_element(By.CLASS_NAME, "gLFyf") #This allows you to get the element you're working, this example we chose the class identifier for the search bar on google

search_bar.clear() #Clear the search bar before sending keys to it. Search bar could already contain text, previous input or even cached values
search_bar.send_keys("Moo Deng" + Keys.ENTER) #This allows you to type into the element
#search_bar.submit() this can be used for websites where the Keys.ENTER doesn't work

'''
Becuase we are trying to access another element here we want to still take the same precaustions as if we did for the search bar 
in the event that we cant find the text Moo Deng. From 33-39 this is meant to click on  the first link that matches Moo Deng.
This does not work with multiple links, the find_element only works with the first link that matches.
'''
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Moo Deng"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Moo Deng")
link.click()

time.sleep(20)

driver.quit()

