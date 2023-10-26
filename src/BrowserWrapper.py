from selenium import webdriver

class BrowserWrapper:
    def __init__(self):
        self.geckoDriverPath = "/usr/local/bin/geckodriver"
        self.service = webdriver.FirefoxService(self.geckoDriverPath)                   # start geckodriver (no args attempts ro download it)
        self.driver = webdriver.Firefox(service=self.service)                           # launch Firefox

    def browse(self):
        self.driver.get("https://www.google.com/")
        print(f"Opened {self.driver.title} ({self.driver.current_url})")

    def close(self):
        self.driver.close()