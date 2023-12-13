import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def setup(request):
    
#     chrome_options = webdriver.ChromeOptions()
#     options = [
#     "--headless=new",
#     "--disable-gpu",
#     "--window-size=1920,1200",
#     "--ignore-certificate-errors",
#     "--disable-extensions",
#     "--no-sandbox",
#     "--disable-dev-shm-usage"
# ]
    options = Options()
    options.add_argument('--headless')

    # for option in options:
    #     chrome_options.add_argument(option)

    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    yield request.cls.driver
    request.cls.driver.close()

