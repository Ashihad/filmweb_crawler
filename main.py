import sys
sys.path.append("src/")     # TODO: switch to module
from BrowserWrapper import BrowserWrapper

import logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s:%(funcName)s() %(message)s", datefmt="[%Y-%m-%d %H:%M:%S]", level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    browser = BrowserWrapper("firefox")
    browser.browse("https://realpython.com/python-logging/")
    browser.close()

if __name__ == "__main__":
    main()