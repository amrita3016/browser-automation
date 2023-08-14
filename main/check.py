from selenium import webdriver 
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
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def clean_text(text):
    """Extreact only temperature from text """
    output = int(text.split(": ")[1])
    return output



def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by ="xpath", value ="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)
print(main())
