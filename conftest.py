import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture(scope='function', params=["chrome"])
def driver(request):
    driver_type = request.param

    if driver_type.lower() == "chrome":
        # chrome_options = ChromeOptions()
        # chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
        # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        # chrome_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif driver_type.lower() == "firefox":
        # firefox_options = FirefoxOptions()
        # firefox_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
        # firefox_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        # firefox_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif driver_type.lower() == "edge":
        # edge_options = EdgeOptions()
        # edge_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
        # edge_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        # edge_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Invalid driver type")

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Browser driver type: chrome, firefox, edge")
