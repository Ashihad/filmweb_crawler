from selenium import webdriver
from selenium.common import exceptions

import logging
logger = logging.getLogger(__name__)

class BrowserWrapper:
    def __init__(self, browserName):
        self.browserName = browserName.lower().strip()
        logger.debug(f"Attempting to init {self.browserName.capitalize()} driver")
        if self.browserName == "firefox":
            self.driverPath = "/usr/local/bin/geckodriver"
            self.service = webdriver.FirefoxService(self.driverPath)                        # start geckodriver (no args attempts to download it)
            try:
                self.driver = webdriver.Firefox(service=self.service)                       # launch Firefox
            except exceptions.SessionNotCreatedException:
                # from None hides traceback from Selenium exception
                raise NoBrowserFound("No Firefox found, please install Firefox") from None
            logger.debug(f"{self.browserName.capitalize()} driver initialized")
        elif self.browserName == "chrome":
            self.driverPath = ""                                                            # I don't care for a specific path atm, since I use Firefox, TODO
            self.service = webdriver.ChromeService()
            try:
                self.driver = webdriver.Chrome(service=self.service)
            except exceptions.SessionNotCreatedException as e:
                # from None hides traceback from Selenium exception
                raise NoBrowserFound("No Chrome found, please install Chrome") from None
            logger.debug(f"{self.browserName.capitalize()} driver initialized")
        else:
            raise NoBrowserFound("Please specify valid browser")

    def browse(self, address):
        self.driver.get(address)
        logger.info(f"Opened \"{self.driver.title}\" ({self.driver.current_url})")

    def close(self):
        self.driver.close()
        logger.info(f"{self.browserName.capitalize()} driver closed")

class NoBrowserFound(Exception):
    pass