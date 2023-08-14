from selenium import webdriver 
import time
from datetime import datetime as dt 

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
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def clean_text(text):
    """Extreact only temperature from text """
    output = int(text.split(": ")[1])
    return output

def write_file(text):
    """Write input text into a text file """
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename,'w') as file:
        file.write(text)
   

def main():
  driver = get_driver()
  while True:
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    text = str(clean_text(element.text))
    write_file(text)
    
print(main())