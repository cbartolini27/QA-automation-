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
       self.driver.get("https://orteil.dashnet.org/cookieclicker/")
    
    #Each test we decide to make MUST first be named 'test'
    def test_example1(self):
        print("WORKED LETS GO!")
        assert True
    
    def test_example2(self):
        print("YOU CAN DO HARD SHIT DUDE!!")
        assert True
    
    def test_title(self):
        mainPage = page.MainPage(self.driver)
       
        if mainPage.in_title_matches() == True:
            print("This worked")
        assert mainPage.in_title_matches()
    
    #Once all of the test cases has run .close() closes the window but webdriver continues to run.
    #.quit() closes all windows and terminates the WebDriver session
    def tearDown(self):
        self.driver.close()
    
    #Says run all of the unit tests we've defined
    if __name__ == '__main__':
        unittest.main()
       
