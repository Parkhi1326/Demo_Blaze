import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
    def test_chrome(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.demoblaze.com/index.html")
            driver.find_element(By.XPATH, "//*[text()='Home ']").click()
            title = driver.title
            assert driver.title == title
        finally:
            driver.close()

    def test_edge(self):
        driver = webdriver.Edge()
        try:
            driver.get("https://www.demoblaze.com/index.html")
            driver.find_element(By.XPATH, "//*[text()='Home ']").click()
            title = driver.title
            assert driver.title == title
        finally:
            driver.close()
# command: pytest -n=2 -v -s C:\Users\parve\PycharmProjects\SDET_10_01\ToolShop_Project\PYTEST\Parallel_Testing.py
# install: pytest-xdist