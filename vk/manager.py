from kutana import VKManager
import json

with open("configuration.json") as fh:
    config = json.load(fh)

vk_manager = VKManager(config["vk_token"])