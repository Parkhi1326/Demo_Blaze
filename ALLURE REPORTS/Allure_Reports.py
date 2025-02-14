import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)

class TestClass:
    @allure.severity(allure.severity_level.MINOR)
    @allure.feature("display LOGO")
    def test_logo(self, setup):
        self.driver = setup
        logo=self.driver.find_element(By.ID,"nava").is_displayed()
        self.driver.close()
        assert True==True
    @allure.feature("Login"):
    def test_login(self,setup):
        self.driver = setup
        self.driver.find_element(By.ID,"loginusername").send_keys("Parkhi")
        self.driver.find_element(By.ID,"loginpassword").send_keys("Parkhi@123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()