import unittest
from selenium.webdriver.chrome.service import Service
import page

from selenium import webdriver
import test_case.page as page #page file we made

class PythonOrgSearch(unittest.TestCase):
    #This is like the __init__ constructer method, use it to set up our variables to test on
    #Tests are running in command promt on windows with the following 
    
    def setUp(self): 
       service = Service(executable_path="C:\\Users\\Christian Bartolini\\QA automation\\QA-automation-\\chromedriver.exe")
       self.driver = webdriver.Chrome(service=service)
       self.driver.get("https://www.google.com/")
    
    #Each test we decide to make MUST first be named 'test'
    def test_example1(self):
        print("heheheh")
        assert True
    
    def test_example2(self):
        assert False
    
    def test_title(self):
        #creating object
        mainPage = page.MainPage()
        assert mainPage.is_title_matches

    
    #Once all of the test cases has run .close() closes the window but webdriver continues to run. .quit() closes all windows and terminates the WebDriver session
    def tearDown(self):
        self.driver.quit()
    
    #Says run all of the unit tests we've defined
    if __name__ == '__main__':
        unittest.main()
       
