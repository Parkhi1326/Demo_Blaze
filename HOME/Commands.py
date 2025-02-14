from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)