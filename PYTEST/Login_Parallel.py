import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestClass:
    def test_login(self, setup):
        driver = setup
        driver.find_element(By.XPATH, "//a[@id='login2']").click()
        driver.find_element(By.ID, "loginusername").send_keys("Parkhi")
        driver.find_element(By.ID, "loginpassword").send_keys("Parkhi@123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()

        assert driver.title == "STORE"
# linked with conftest.py file