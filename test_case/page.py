import locator
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q" #This is the name for the search box
 
class BasePage(object):                                         
    def __init__(self, driver):
        #instance variable
        self.driver = driver

#inhereting BasePage
class MainPage(BasePage):
    #Creates an instance of the SearchTextElement() class above.
    search_text_element = SearchTextElement()
    
    

    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*locator.MainPageLocators.GO_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

class SearchResultPage(BasePage):
    def is_results_found(self):
        #Each new page should incorporate this if you are doing a data retreival function
        return "No results found." not in self.driver.page_source #Returns true if 'No results found.' is not on the page. If its not on the page search was successful




