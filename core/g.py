from core.config import Config


config: Config = None


def init():
    global config
    config = Config()
    config.load("config/conf.yaml")
