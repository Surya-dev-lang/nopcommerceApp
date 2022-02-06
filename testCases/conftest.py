from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(broswer):
    if broswer == 'chrome':
        options = Options()
        options.add_argument("start-maximized")
        #driver = webdriver.Chrome(executable_path="/Users/macbookpro/Documents/Selenium/chromedriver")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),  options=options)
    else:
        options = Options()
        options.add_argument("start-maximized")
        # driver = webdriver.Chrome(executable_path="/Users/macbookpro/Documents/Selenium/chromedriver")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def pytest_addoption(parser):  # This will get value from the CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def broswer(request):         # This will return the browser value to setup method
    return request.config.getoption('--browser')


############PyTest HTML Report##############

#Adding additional info to the HTML report
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Surya'

#Hook to delete/modify environment info in the HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
