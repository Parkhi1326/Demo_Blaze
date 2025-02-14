import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

# scroll down by pixel:
driver.execute_script("window.scrollBy(0,500)","")
value=driver.execute_script("return window.pageYOffset;")
print("No of pixel moved: ",value)
time.sleep(4)

# scroll till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("No of pixel moved: ",value)
time.sleep(4)

#scroll at top of page:
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("No of pixel moved: ",value)
time.sleep(4)