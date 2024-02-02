from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.baseclass import BaseClass

class LoginPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)


    
    loginpage_text_xpath = "//div[@class = 'page-title']/h1"
    email_xpath = "//*[@id='Email']"
    password_xpath = "//*[@id='Password']"
    checkbox_xpath = "//div[@class= 'inputs reversed']/input[@type='checkbox']"
    submit_xpath = "//div[@class= 'buttons']/button[@type='submit']"
    invalid_email_xpath = "//form[@method='post']/div/ul/li"
    error_warning = "//div[@class='inputs']/span/span"
    

    def loginpage_text(self):
        return self.check_for_text("loginpage_text_xpath", self.loginpage_text_xpath)

    def input_email_and_password(self, email, password):
        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[2].value = arguments[3];", self.get_element("email_xpath", self.email_xpath), email, self.get_element("password_xpath", self.password_xpath), password)

    def click_checkbox(self):
        self.element_click("checkbox_xpath", self.checkbox_xpath)

    def click_submit(self):
        self.element_click("submit_xpath", self.submit_xpath)

    def invalid_email_error(self):
        return self.check_for_text("invalid_email_xpath", self.invalid_email_xpath)
    
    def error_message(self):
        return self.check_for_text("email_xpath", self.email_xpath)

        