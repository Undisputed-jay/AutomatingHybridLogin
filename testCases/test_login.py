from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pytest

from pageobject.loginpage import LoginPage 
from pageobject.accountpage import AccountPage
from pageobject.basetest import BaseTest

from utilities import excelutils

class TestLogin(BaseTest):

    @pytest.mark.parametrize("email, password", excelutils.get_data_from_excel(path = "./testCases/excelFile/login_details.xlsx", sheet_name = "Login"))
    def test_login_with_all_details(self, email, password):

        loginpage = LoginPage(self.driver)
        accountpage = AccountPage(self.driver)
        expected_message = "Admin area demo"
        actual_message = loginpage.loginpage_text()
        assert expected_message.__eq__(actual_message)
        loginpage.input_email_and_password(email, password)
        loginpage.click_checkbox()
        loginpage.click_submit()
        expected_message_1 = "Dashboard"
        actual_message_1 = accountpage.displayed_message()
        assert actual_message_1.__eq__(expected_message_1)

    @pytest.mark.parametrize("password", excelutils.get_data_from_excel(path = "./testCases/excelFile/login_details.xlsx", sheet_name = "Login"))
    def test_login_with_invalid_email(self, password):
        loginpage = LoginPage(self.driver)
        expected_message = "Admin area demo"
        actual_message = loginpage.loginpage_text()
        assert expected_message.__eq__(actual_message)
        loginpage.input_email_and_password(self.generate_email_with_timestamp(), password)
        loginpage.click_checkbox()
        loginpage.click_submit()
        expected_error = "No customer account found"
        actual_error = loginpage.invalid_email_error()
        assert actual_error.__contains__(expected_error)

    def test_login_with_invalid_password(self):
        loginpage = LoginPage(self.driver)
        expected_message = "Admin area demo"
        actual_message = loginpage.loginpage_text()
        assert expected_message.__eq__(actual_message)
        loginpage.input_email_and_password("admin@yourstore.com", "123456")
        loginpage.click_checkbox()
        loginpage.click_submit()
        expected_error = "The credentials provided are incorrect"
        actual_error = loginpage.invalid_email_error()
        assert actual_error.__contains__(expected_error)

    def test_login_without_entering_any_details(self):
        loginpage = LoginPage(self.driver)
        expected_message = "Admin area demo"
        actual_message = loginpage.loginpage_text()
        assert expected_message.__eq__(actual_message)
        loginpage.input_email_and_password("", "")
        loginpage.click_submit()
        expected_error = "Please enter your email"
        actual_error = loginpage.error_message()
        assert expected_error.__contains__(actual_error)



