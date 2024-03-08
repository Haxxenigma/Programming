from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

api_key = config["OpenAI"]["api_key"]
chat_id = config["Telegram"]["chat_id"]
token = config["Telegram"]["token"]
api_id = config["Telegram"]["api_id"]
api_hash = config["Telegram"]["api_hash"]
username = config["Telegram"]["username"]
