from configparser import ConfigParser
from os.path import dirname

base_dir = dirname(__file__)

config = ConfigParser()
config.read(base_dir + "/config.ini")

api_key = config["OpenAI"]["api_key"]
api_id = config["Telegram"]["api_id"]
api_hash = config["Telegram"]["api_hash"]
token = config["Telegram"]["token"]
phone = config["Telegram"]["phone"]
password = config["Telegram"]["password"]
