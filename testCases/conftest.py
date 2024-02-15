from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from allure_commons.types import AttachmentType

from utilities.readconfigurations import read_configurations

@pytest.fixture(autouse=True)
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name = "failed_test", attachment_type= AttachmentType.PNG)

@pytest.hookimpl(hookwrapper = True, tryfirst= True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+ rep.when, rep)
    return rep


@pytest.fixture
def setup_and_teardown(request):
    browser = read_configurations("basic info", "browser")
    global driver
    driver = None
    if browser.__eq__("chrome"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Which browser am i using?")
    driver.maximize_window()
    app_url = read_configurations("basic info", "url")
    driver.get(app_url)
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.quit()
    
