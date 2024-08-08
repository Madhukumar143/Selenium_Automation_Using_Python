import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Hybrid_framework.tests.utilities import ReadConfigurations

@pytest.fixture()
def log_on_result(request):
    yield
    item = request.node
    if item.rep_call.failed:
        #screenshot for failed case
        allure.attach(driver.get_screenshot_as_png(), name="Failed_Screenshot", attachment_type=AttachmentType.PNG)
    elif item.rep_call.passed:
        # Attach screenshot for passed test cases
        allure.attach(driver.get_screenshot_as_png(), name="Passed_Screenshot", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture() # we can use autouse, scope as parameters here
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    driver.maximize_window()
    cur_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(cur_url)
    request.cls.driver = driver
    yield
    driver.quit()
    #print("Test cases are executed")