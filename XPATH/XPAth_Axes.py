from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

laptops_element = driver.find_element(By.XPATH, "//*[text()='Laptops']")
children = driver.find_elements(By.XPATH, "//*[text()='Laptops']/following-sibling::*")
print("Children Count:", len(children))

parent = driver.find_elements(By.XPATH, "//*[text()='Laptops']/parent::*")
print("Parent Count:", len(parent))

ancestors = driver.find_elements(By.XPATH, "//*[text()='Laptops']/ancestor::*")
print("Ancestors Count:", len(ancestors))

following = driver.find_elements(By.XPATH, "//*[text()='Laptops']/following::*")
print("Following Count:", len(following))

preceding = driver.find_elements(By.XPATH, "//*[text()='Laptops']/preceding::*")
print("Preceding Count:", len(preceding))

preceding_sibling = driver.find_elements(By.XPATH, "//*[text()='Laptops']/preceding-sibling::*")
print("Preceding Sibling Count:", len(preceding_sibling))

descendants = driver.find_elements(By.XPATH, "//*[text()='Laptops']/ancestor::*//descendant::*")
print("Descendants Count:", len(descendants))
driver.quit()