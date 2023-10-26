import sys
sys.path.append("src/")     # TODO: switch to module
from BrowserWrapper import BrowserWrapper

def main():
    browser = BrowserWrapper()
    browser.browse()
    browser.close()

if __name__ == "__main__":
    main()