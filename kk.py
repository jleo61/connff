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
class Locators:
    def __init__(self, driver):
        self.driver = driver

        self.radio_button_xpath = "//div[@id = 'radio-btn-example']/fieldset/label[2]/input"
        self.seggestion1_xpath = "//*[@id='autocomplete']"
        self.dro_down_optio = "//*[@id='dropdown-class-example']"
        self.check_box = "//*[@id='checkBoxOption1']"
        self.windo_switch = "//*[@id='openwindow']"
        self.choice = ["us", "eth", "au", "eng", "eri"]
        self.alert_xpath = "//*[@id='alertbtn']"
        self.table_amount = "//div[@class = 'tableFixHead']/table/tbody/tr/td[4]"
        self.mouse_hover = "//*[@id='mousehover']"
        self.new_tab = "//*[@id='opentab']"
        self.iframe_xpath = "//*[@id='courses-iframe']"

        self.book = openpyxl.load_workbook("home_page.xlsx")
        self.home_sheet = self.book.active

    def test_autoseggest(self):
        self.driver.find_element(By.XPATH, self.seggestion1_xpath).send_keys("ga")
        time.sleep(2)
        j = self.driver.find_element(By.XPATH, self.seggestion1_xpath).get_attribute("value")
        print("User entered", j, "on the country field")
        # self.home_sheet.cell(row = 1, column=1, value="test_autoseggest")
        # self.home_sheet.cell(row = 1, column=2, value=j)