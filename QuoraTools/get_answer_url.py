from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = input("Enter the URL of the Question: ")

options = Options()
options.add_argument("--window-size=1920x1080")
chromedriver_path = './chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
driver.get(url)
f = open('q_links.txt', 'w')
current_height = driver.execute_script("return document.body.scrollHeight")

while True:
   # Scroll down by two pages
   driver.execute_script("window.scrollBy(0, 2*1080);")
   # Wait for the page
   time.sleep(3)
   # get page height in px
   new_height = driver.execute_script("return document.body.scrollHeight")
   # break this loop when you are not able to scroll futher
   if new_height == current_height:
      break
   current_height = new_height

html_source = driver.find_elements_by_xpath("//a[@class='answer_permalink']")
i=0
for x in html_source:
    anslink = x.get_attribute('href')
    f.write(anslink+"\n")
    i+=1
    
f.close()
print("Quitting Chrome after adding "+str(i)+" links.")
driver.quit()
