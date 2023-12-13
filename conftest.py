import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    
    

    request.cls.driver = webdriver.Chrome()
    yield request.cls.driver
    request.cls.driver.close()
