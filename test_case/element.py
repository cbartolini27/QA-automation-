from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
"""
Represents one element on the page. For example it would represent a search bar or a form input. What this element
page is saying is don't worry about using the WebDriverWait anymore, we'll set up this base object that anytime 
we try to set or get an elements value we will automatically implement the WebDriverWait functionality. This 
will be hidden behind the scenes but what this allows us to do is whenever we want to access a new element we no 
longer have to implement the WebDriverWait we can just use the BasePageElement class.

When you are interacting with a new page you DO NOT need to create another class in here. You can re-use the same class. You
can create a new class if you want to deal with different identifiers. In this class we are working with the NAME identifier
but what if we want to work with the ID identifer? Then we would create a new class, copy the existing code that we already 
have for BasePageElement(object) class and change By.NAME to By.ID. We have to create a new class for each identifer since 
this is seen in python as a descripter, and python would get confused with multiple __set__ and __get__ methods.

"""
#Setting the value of the element - descriptor class
class BasePageElement(object):
    #Setting and getting the 'name' element. If you want ID you would maybe have to create another set of these
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator)
        )
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator)
        )
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute("value")