import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

@pytest.fixture()
def log_on_result(request):
    yield
    item = request.node
    if item.rep_call.failed:
        #screenshot for failed case
        allure.attach(driver.get_screenshot_as_png(), name="Negetive Search", attachment_type=AttachmentType.PNG)
    elif item.rep_call.passed:
        # Attach screenshot for passed test cases
        allure.attach(driver.get_screenshot_as_png(), name="Success Screenshot", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture() # we can use autouse, scope as parameters here
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
    print("Test cases are executed")
