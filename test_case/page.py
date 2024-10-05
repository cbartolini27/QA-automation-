import locator
class BasePage(object):
    def __init__(self, driver):
        #instance variable
        self.driver = driver

#inhereting BasePage
class MainPage(BasePage):
    def in_title_matches(self):
        return "Cookie Clicker" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*locator.MainPageLocators.COOKIE)
        self.driver.execute_script("arguments[0].click();", element)

class SearchResultPage(BasePage):
    
    def is_results_found(self):
        return "No results found." not in self.driver.page_source




