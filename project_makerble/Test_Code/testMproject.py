from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Test_Data import project_4
import pytest
import time 

class Test_Project_4:
    url = "https://qa.makerble.com/users/sign_up " 

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Edge()
        yield
        self.driver.close() 
           
    def test_sign(self, booting_function):
        
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=project_4.Project_Selector_1.firstname_id).send_keys(project_4.Project_Data_1.first_name)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=project_4.Project_Selector_1.lastname_id).send_keys(project_4.Project_Data_1.last_name)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=project_4.Project_Selector_1.email_id).send_keys(project_4.Project_Data_1.email)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=project_4.Project_Selector_1.email_confirmation_id).send_keys(project_4.Project_Data_1.email_confirmation)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=project_4.Project_Selector_1.password_id).send_keys(project_4.Project_Data_1.password)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=project_4.Project_Selector_1.password_confirmation_id).send_keys(project_4.Project_Data_1.password_confirmation)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.choosefile_xpath).send_keys('C:\\Users\\neeth\\OneDrive\\Pictures\\Screenshots\\flower.jpg')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/form/div[8]').click()
        time.sleep(40)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.signup_xpath).click()
        time.sleep(3)
        
        print("signed up successfully")
        
    def test_login(self, booting_function):
        
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.signin_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.user_email_xpath).send_keys(project_4.Project_Data_1.user_email)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.user_password_xpath).send_keys(project_4.Project_Data_1.user_password)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.login_signin_xpath).click()
        time.sleep(2)   
        #self.driver.find_element(by=By.XPATH, value='//*[@id="termsConditionsCheckbox"]').click()
        #time.sleep(5)
        print("loggedin successfully")
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.organization_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.organization_name).send_keys(project_4.Project_Data_1.org_name)
        time.sleep(2)
        ele_one = Select(self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.country_xpath))
        ele_one.select_by_visible_text('India')
        time.sleep(2)
        ele_two = Select(self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.organization_type_xpath))
        ele_two.select_by_visible_text('Company')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="charity_terms_checkbox"]').click() 
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value =project_4.Project_Selector_1.make_new_xpath).click() 
        time.sleep(10)
        
    def test_new(self,booting_function):
        
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.signin_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.user_email_xpath).send_keys(project_4.Project_Data_1.user_email)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.user_password_xpath).send_keys(project_4.Project_Data_1.user_password)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.login_signin_xpath).click()
        time.sleep(2)   
        self.driver.find_element(by=By.XPATH, value='//*[@id="main_header_div"]/div[1]/div[2]/ul[1]/li[2]/a')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value =project_4.Project_Selector_1.create_project_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value =project_4.Project_Selector_1.project_name_xpath).send_keys(project_4.Project_Data_1.project_name)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="new_project"]/div[5]/button').click()
        time.sleep(4)
        
    def test_list(self,booting_function):
        
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.signin_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.user_email_xpath).send_keys(project_4.Project_Data_1.user_email)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.user_password_xpath).send_keys(project_4.Project_Data_1.user_password)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.login_signin_xpath).click()
        time.sleep(2)   
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.myapps_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.categories_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.new_categorylist_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.list_fieldname_xpath).send_keys(project_4.Project_Data_1.list_fieldname)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.item1_xpath).send_keys(project_4.Project_Data_1.item_1)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.item2_xpath).send_keys(project_4.Project_Data_1.item_2)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.additem_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.removeitem_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.advanced_option_xpath).click()
        time.sleep(3) 
        ele_three =Select(self.driver.find_element(by=By.XPATH, value='//*[@id="ratio_set_ratio_category_id"]'))
        ele_three.select_by_visible_text('abc')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=project_4.Project_Selector_1.save_1_xpath).click()
        time.sleep(3)
        print("List fields are created") 
        time.sleep(3)
        