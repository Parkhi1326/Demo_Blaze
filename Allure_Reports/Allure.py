import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)
class Test_Demo:
    @allure.severity(allure.severity_level.NORMAL)
    def test_logo(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        status=self.driver.find_element(By.XPATH,"//*[text()='Home ']").is_displayed()
        if status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_category(self):
        pytest.skip("skipping the test process here....")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.ID,"loginusername").send_keys("Parkhi")
        self.driver.find_element(By.ID,"loginpassword").send_keys("Parkhi@123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(5)
        act_title=self.driver.title
        if act_title=="STORE":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="passed scenario",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

            # C:\Users\parve\PycharmProjects\SDET_10_01\ToolShop_Project\Allure_Reports
# command : pytest -v -s --alluredir="C:\Users\parve\PycharmProjects\SDET_10_01\ToolShop_Project\Allure_Reports\Reports" Allure_reports\Allure.py

# steps to open allure reports: copy reports folder path-open cmd-type allure serve and paste the path till reports folder-enter
# C:\Users\parve\PycharmProjects\SDET_10_01\ToolShop_Project\Allure_Reports\Reports