from configparser import ConfigParser
from pprint import pprint


class ProgramConfig:
    """Class that stores global program configuration, read from a configFile file"""
    def __init__(self, configPath="config.ini"):
        self.configPath = configPath
        self.config = None

    def parse(self):
        self.config = ConfigParser()
        self.config.read(self.configPath)
        raw_dict = self.config._sections
        return raw_dict