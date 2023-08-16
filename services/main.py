from models.api import API
from models.exchange import BinanceExchange
from pprint import pprint

if __name__ == "__main__":
    api = API()
    binance_exchange = BinanceExchange(api=api)
    pprint(binance_exchange.get_advertises(pay_type="RosBankNew", asset="USDT", fiat="RUB").json())