from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()


@pytest.mark.usefixtures("setup")
class TestWan:
    def test_one(self):
        print("Working")