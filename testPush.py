from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


print("Hello World")

#Testing single line with python rn
'''
Just testing multilined with python rn
'''