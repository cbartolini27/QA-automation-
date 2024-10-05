'''
Any way we locate an element should be keep in one centralized location so that if we ever need to its very easy to change the ID.
MainPageLocater is a class for the Main Page where if theres any attributes on the page in which we want to access, we should define
how we want to access them (by ID, Class, etc.) and what their value is.

'''
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    COOKIE = (By.ID, "bigCookie")