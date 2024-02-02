from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageobject.baseclass import BaseClass

class AccountPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)


    message_xpath = "//*[@class='content-header']/h1"

    def displayed_message(self):
        return self.check_for_text("message_xpath", self.message_xpath)

    