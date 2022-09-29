import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service = Service(TestData.CHROME_EXECUTABLE_PATH))
    request.cls.driver = web_driver
    yield
    web_driver.close()