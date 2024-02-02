from selenium import webdriver
from selenium.webdriver.common.by import By

# this acts as a parent classs for all the pages

class BaseClass:
    
    def __init__(self, driver):
        self.driver = driver
    
    # defining an element that can be used in all function
    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.__contains__("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        return element
    
    def type(self, text, locator_name, locator_value):
        
        element = self.get_element(locator_name, locator_value)
        # performing operations on the element
        element.click()
        element.clear()
        element.send_keys(text)
        
    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        
    def check_if_displayed(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()
    
    def check_for_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text
    