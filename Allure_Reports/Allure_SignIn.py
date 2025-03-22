import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)
class Test_SignIn:
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
    def test_signin(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.ID, "sign-username").send_keys("Parkhi")
        self.driver.find_element(By.ID,"sign-password").send_keys("Parkhi@123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign up']").click()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "STORE":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="passed scenario",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False