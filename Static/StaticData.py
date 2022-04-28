import json


class StaticData:
    ShopData = None

    @classmethod
    def preload(cls):
        cls.ShopData = json.loads(open("Static/Shop.json", "r").read())
