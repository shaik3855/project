from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Orange_Data
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
        self.driver.get(Orange_Data().url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Web Title Captured")
   
    def test_TC_PIM_01(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click()

        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()

        # Click on the "Add Employee" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.add_employee_button).click()

        # Click on the "Add Photo" button and upload the photo
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.photo_add_button).click()
        self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(Orange_Locators().file_path)

        # Enter the employee's first name, middle name, and last name
        self.driver.find_element(by=By.NAME, value=Orange_Locators.first_name_locator).send_keys(Orange_Locators.first_name)
        self.driver.find_element(by=By.NAME, value=Orange_Locators.middle_name_locator).send_keys(Orange_Locators.middle_name)
        self.driver.find_element(by=By.NAME, value=Orange_Locators.last_name_locator).send_keys(Orange_Locators.last_name)

        # Click on the "Save" button to save the employee's basic information
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_1).click()

        # Enter the employee's street 1, street 2, city, and work email
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.contact_details_button).click()
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.street_1_locator).send_keys(Orange_Locators.street_1)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.street_2_locator).send_keys(Orange_Locators.street_2)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.city_locator).send_keys(Orange_Locators.city)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.email_locator).send_keys(Orange_Locators.work_email)

        # Click on the "Save" button to save the employee's contact details
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_2).click()
        assert self.driver.title =='OrangeHRM'
        print("successfully employee added")

    
         
    