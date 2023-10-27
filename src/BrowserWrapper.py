from selenium import webdriver
from selenium.common import exceptions

import logging
logger = logging.getLogger(__name__)

class BrowserWrapper:
    def __init__(self, browserName, driverPath):
        self.browserName = browserName.lower().strip()
        self.driverPath = driverPath
        logger.debug(f"Attempting to init {self.browserName.capitalize()} driver")
        if self.browserName == "firefox":
            self.service = webdriver.FirefoxService(self.driverPath)                        # start geckodriver (no args attempts to download it)
            try:
                self.driver = webdriver.Firefox(service=self.service)                       # launch Firefox
            except exceptions.SessionNotCreatedException:
                raise NoBrowserFound("No Firefox found, please install Firefox") from None
        elif self.browserName == "chrome":
            self.service = webdriver.ChromeService(self.driverPath)
            try:
                self.driver = webdriver.Chrome(service=self.service)
            except exceptions.SessionNotCreatedException as e:
                raise NoBrowserFound("No Chrome found, please install Chrome") from None
        elif self.browserName == "edge":
            self.service = webdriver.EdgeService(self.driverPath)
            try:
                self.driver = webdriver.Edge(service=self.service)
            except exceptions.SessionNotCreatedException as e:
                raise NoBrowserFound("No Edge found, please install Edge") from None
        else:
            raise NoBrowserFound("Please specify valid browser")
        logger.debug(f"{self.browserName.capitalize()} driver initialized")

    def browse(self, address):
        self.driver.get(address)
        logger.info(f"Opened \"{self.driver.title}\" ({self.driver.current_url})")

    def close(self):
        self.driver.close()
        logger.info(f"{self.browserName.capitalize()} driver closed")

class NoBrowserFound(Exception):
    pass

if __name__ == "__main__":
    print("BrowserWrapper class")