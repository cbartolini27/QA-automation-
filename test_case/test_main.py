import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import test_case.page as page #page file we made
import page

class PythonOrgSearch(unittest.TestCase):
    #This is like the __init__ constructer method, use it to set up our variables to test on
    def setUp(self): 
       service = Service(executable_path="chromedriver.exe")
       self.driver = webdriver.Chrome(service=service)
       self.driver.get("https://www.python.org/")
    
    #Each test we decide to make MUST first be named 'test'
    def test_title(self):
        main_page = page.MainPage(self.driver)
       
        if main_page.is_title_matches() == True:
            print("This worked")
        self.assertTrue(main_page.is_title_matches(), "Python is not in the title!") #Different way of asserting true or not
    
    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        
        #Inputing or setting "pycon" into the search bar element
        main_page.search_text_element = "pycon" #.search_text_element isn't seen as an object or instance but rather a descripter
        main_page.click_go_button()
        
        #After clicking on the search bar we now have a different page. Then we check to see if we were given No results for that search
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    #Once all of the test cases has run .close() closes the window but webdriver continues to run.
    #.quit() closes all windows and terminates the WebDriver session
    def tearDown(self):
        self.driver.close()
    
    #Says run all of the unit tests we've defined
    if __name__ == '__main__':
        unittest.main()