import locator
from element import BasePageElement
from selenium.webdriver.common.by import By



 
class BasePage(object):                                         
    def __init__(self, driver):
        #instance variable
        self.driver = driver

#inhereting BasePage
class MainPage(BasePage):
    #Creates an instance of the SearchTextElement() class above.
    #Now able t
    search_text_element = BasePageElement(By.NAME, locator.MainPageLocators.SEARCH_BOX)
    
    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*locator.MainPageLocators.GO_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

class SearchResultPage(BasePage):
    def is_results_found(self):
        #Each new page should incorporate this if you are doing a data retreival function
        return "No results found." not in self.driver.page_source #Returns true if 'No results found.' is not on the page. If its not on the page search was successful




