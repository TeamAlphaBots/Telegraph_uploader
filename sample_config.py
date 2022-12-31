import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("5096441059:AAF6jv5_6pgR3Ia8ObCtY2tHUjCiHRiIiTQ", "")

    APP_ID = int(os.environ.get("APP_ID", 7721764))

    API_HASH = os.environ.get("API_HASH", "a9c08aae19aa4c8b37ff658d1951a1f7")
