from strategymanager import strategy as str, strinyector as stryec
from datamanager import dataprovider as dp

class Bot:
    def __init__(self, strategy: str.Strategy, dataProvider: dp.DataProvider):
        self.deals = []
        self.strategy = strategy
        self.dataProvider = dataProvider



