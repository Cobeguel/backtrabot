from datamanager import dataprovider
import pandas as pd
import numpy as np

class BinanceDP(dataprovider.DataProvider):
    def __init__(self, dataSource):
        super().__init__(dataSource)
        self.data = self.__read_file()

    def __read_file(self):
        try:
            names=['date','open','high','low','close','volume']
            data=pd.read_csv(self.dataSource, names=names, usecols=[0,1,2,3,4,5])
            data['date'] = pd.to_datetime(data['date'],unit='ms')
            return data
        except Exception as e:
            print("An error has ocurred: " + e)

        