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

    def test_TC_PIM_02(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click()

        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()

        # Click on the "employee_list" button    
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()

        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field)

        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()

        # Click on the "edit_button" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.edit_button).click()

        # Click on the "nickname_locator" and enter the "name_field"
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.nickname_locator).send_keys(Orange_Locators.name_field)

        # Click on the "Save" button to save the employee's added details
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.save_button_3).click()
        assert self.driver.title =='OrangeHRM'
        print("successfully employee additional details added")


    def test_TC_PIM_03(self, boot):
        self.driver.get(Orange_Data().url)
        self.driver.implicitly_wait(10)
        # login details with click "submit" button
        self.driver.find_element(by=By.NAME, value=Orange_Locators().username_input_box).send_keys(Orange_Data().Username)
        self.driver.find_element(by=By.NAME, value=Orange_Locators().password_input_box).send_keys(Orange_Data().Password)
        self.driver.find_element(by=By.XPATH, value=Orange_Locators().submit_button).click()

        # Click on the "pim" button
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.PIM_button).click()  

        # Click on the "employee_list" button  
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_list_button).click()

        # Click on the "mployee_id_locator" and enter the "id_field" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.employee_id_locator).send_keys(Orange_Locators.id_field_1)

        # Click on the "searchbox_locator" 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.searchbox_locator).click()
        # Click on the "delete" button 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.delete_button).click()
        
        # Click on the "reconfirm_delete" button 
        self.driver.find_element(by=By.XPATH, value=Orange_Locators.reconfirm_delete_button).click()
        assert self.driver.title =='OrangeHRM'
        print("successfully employee deleted")       