from configparser import ConfigParser
from os import path

base_dir = path.dirname(path.realpath(__file__))

config = ConfigParser()
config.read(base_dir + "/config.ini")

login = config["Credentials"]["login"]
password = config["Credentials"]["password"]
