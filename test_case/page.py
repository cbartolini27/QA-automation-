class BasePage(object):
    def __init__(self, driver):
        #instance variable
        self.driver = driver

#inhereting BasePage
class MainPage(BasePage):
    def in_title_matches(self):
        return "Cookie Clicker" in self.driver.title
    
