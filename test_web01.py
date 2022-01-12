import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('http://nytimes.com')
        print(self.driver.title)