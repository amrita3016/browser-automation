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
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver


def main():
  driver = get_driver()
  # Find and fill in username and password 
  driver.find_element(by="id", value="CustomerEmail").send_keys("app7flask@gmail.com")
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys("??!65EhGMg8.WwY" + Keys.RETURN)
  time.sleep(2)

  # Click on Home link and wait 2 sec
  driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
  time.sleep(2)
  print(driver.current_url)

print(main())