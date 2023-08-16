from abc import ABC, abstractmethod
from models.api import API
from fake_useragent import UserAgent

FakeUserAgent = UserAgent()


class Exchange(ABC):
    def __init__(self, api: API):
        self.api = api

    @abstractmethod
    def payment_methods(self):
        pass

    @abstractmethod
    def available_currencies(self):
        pass

    @abstractmethod
    def get_advertises(self, pay_type: str, asset: str, fiat, count: int, limit: float):
        pass


class BinanceExchange(Exchange):
    def payment_methods(self):
        ...

    def available_currencies(self):
        ...

    def get_advertises(self, pay_type, asset, fiat, count=10, limit=0.0):
        url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
        headers = {
            "Accept": "*/*",
            "Content-type": "application/json",
            "Origin": "https://p2p.binance.com",
            "User-Agent": FakeUserAgent.random
        }
        params = {"page": 1, "rows": count, "payTypes": [pay_type], "countries": [], "asset": asset,
                  "tradeType": "BUY", "fiat": fiat, "transAmount": f"{limit}"}
        binance_advertises = self.api.post(url=url, json=params, headers=headers)
        return binance_advertises
