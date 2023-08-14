from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

#PATH = r"./chromedriver.exe"
driver = webdriver.Chrome()

#driver.get("https://automated.pythonanywhere.com/")

def get_driver():  
  #SET OPTIONS TO MAKE BROWSING EASIER
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars") #flags which create problems while accessing script
  options.add_argument("start-maximized") #so that website content is not changed when resize
  options.add_argument("disable-dev-shm-usage")  #avoid errors in a linux machine
  options.add_argument("no-sandbox") #to disable sandbox
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disble-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login")
  return driver


def main():
  driver = get_driver()
  driver.find_element(by ="id", value ="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by ="id", value ="id_password").send_keys("automatedautomated" + Keys.RETURN)
  print(driver.current_url)
  time.sleep(2)
  driver.find_element(by="xpath",value="/html/body/div/nav/a").click()
  print(driver.current_url)
print(main())