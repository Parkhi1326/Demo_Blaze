import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)
class Test_Contact:
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.XPATH,"//*[text()='Contact']").click()
        self.driver.find_element(By.ID,"recipient-email").send_keys("parkhigera@gmail.com")
        self.driver.find_element(By.ID,"recipient-name").send_keys("Parkhi")
        self.driver.find_element(By.ID,"message-text").send_keys("hello everyone")
        self.driver.find_element(By.XPATH,"//*[text()='Send message']").click()
        time.sleep(4)
        try:
            alert = Alert(self.driver)
            allure.attach(alert.text, name="Alert Message",
                          attachment_type=AttachmentType.TEXT)
            alert.accept()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Alert Error", attachment_type=AttachmentType.PNG)
            allure.attach(str(e), name="Exception", attachment_type=AttachmentType.TEXT)
        allure.attach(self.driver.get_screenshot_as_png(), name="After Alert", attachment_type=AttachmentType.PNG)
        self.driver.close()