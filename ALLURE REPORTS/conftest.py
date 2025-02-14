from ast import parse

from selenium import webdriver

import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        driver.get("https://www.demoblaze.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver
    elif browser=="edge":
        driver=webdriver.Edge()
        driver.get("https://www.demoblaze.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver
    elif browser=="firefox":
        driver=webdriver.Firefox()
        driver.get("https://www.demoblaze.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
# command to execute code till line 31:    pytest -s -v --html=path path