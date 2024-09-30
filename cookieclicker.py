from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys #In tutorial theres no import for key in boilerplate
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie_id = "bigCookie"

#Function for getting the cookie count
def get_cookie_count():
    #Find the element div containing the cookie count and grab the text
    cookie_count_text = driver.find_element(By.ID, 'cookies').text #.text seleniums way of extracting visible text from the element we find
    
    '''
    Remember we are pulling a string out of this so we need to parse, split(" ") 
    is a Python method which splits the string into a list of substrings.
    [0] grabs the first element in the list. We want to do this becuase if we 
    were to just do cookie_count_text[0] it would only grab the first element
    and if we have '128' clicks for our cookie, it will only grab '1'
    '''
    cookie_count = int(cookie_count_text.split(" ")[0])
    return cookie_count


#Wait for the language to appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)

#Click on the language (English)
language = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
language.click()






#Clicking the cookie
while (get_cookie_count() < 100):
    try:
        #Wait for the Cookie to appear
        WebDriverWait(driver, 5).until(
         EC.presence_of_element_located((By.ID, cookie_id))
        )
        
        time.sleep(0.01)
        cookie = driver.find_element(By.ID, cookie_id)
        driver.execute_script("arguments[0].click();", cookie) #Used javaScript to click cookie b/c ran into selenium issues
    
    except Exception as e:
        print(f"Error clicking the cookie: {e}")

time.sleep(120)