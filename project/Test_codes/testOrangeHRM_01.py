from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data_1 import Orange_Data_1
from Test_Locators.locators import Orange_Locators
import pytest

class Test_OrangeHRM:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.quit()
   
    def test_get_title(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Orange_Data_1().url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Web Title Captured")

    def test_TC_Login_01(self, boot):
        self.driver.get(Orange_Data_1().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data_1().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data_1().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click()    
        print("Invalid Credentials")
    