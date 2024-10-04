from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys #In tutorial theres no import for key in boilerplate
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
import time

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
product_price_prefix = "productPrice"
upgrade_prefix = "product"

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
    
    cookie_count = cookie_count_text.split(" ")[0] #Parsing to grab first number before space in string
    cleaned_cookie_count = int(cookie_count.replace(",", "")) #Replacing a semicolon
   
    return cleaned_cookie_count


#Wait for the language to appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)

#Click on the language (English)
language = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
language.click()


#Clicking the cookie and buying upgrades
while True:
    try:
        time.sleep(0.3) # Resolved printing payment successful out to many times
        number_of_cookies = get_cookie_count()
       
        #Wait for the Cookie to appear
        WebDriverWait(driver, 5).until(
         EC.presence_of_element_located((By.ID, cookie_id))
        )
        
        cookie = driver.find_element(By.ID, cookie_id)
        driver.execute_script("arguments[0].click();", cookie) #Used javaScript to click cookie b/c ran into selenium issues
       
       #Getting the price for each upgrade, 20 possible ones to get
        for i in range(20):
            upgrade_price = driver.find_element(By.ID, product_price_prefix + str(i)).text
            cleaned_upgrade_price = int(upgrade_price.replace(",", "")) #gets rid of commas when getting the price
    
            
            if number_of_cookies >= cleaned_upgrade_price:
               upgrade = driver.find_element(By.ID, upgrade_prefix + str(i))
               driver.execute_script("arguments[0].click();", upgrade)
               break
    except Exception as e:
        pass



    
    
time.sleep(120)