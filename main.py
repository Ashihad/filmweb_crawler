import sys
sys.path.append("src/")     # TODO: switch to module
from ConfigParser import ProgramConfig
from BrowserWrapper import BrowserWrapper
from typing import Dict

import logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s:%(funcName)s() %(message)s", datefmt="[%Y-%m-%d %H:%M:%S]", level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    cfgParser = ProgramConfig()
    config: Dict[str, str] = cfgParser.parse()

    browser = BrowserWrapper(config["driver"]["drivertype"], config["driver"]["driverpath"])
    browser.browse("https://filmweb.pl")
    browser.close()

if __name__ == "__main__":
    main()