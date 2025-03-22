import pytest
from selenium import webdriver

@pytest.fixture()
def setup(request):  # Ensure pytest can inject the fixture
    browser = request.config.getoption("--browser")  # Get browser option
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Invalid browser option")

    driver.get("https://www.demoblaze.com/index.html")
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver  # Ensures proper cleanup
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
