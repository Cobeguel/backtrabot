#import Bot
from datamanager.managers.binance import BinanceDP

if __name__ == "__main__":
    sourceFile = 'data/binance/ada/ADAUSDT-5m-2021-11.csv'
    pairData = BinanceDP(sourceFile)
    print(pairData.data)


    """
    if __name__ == "__main__":
        sourceFile = "tests/data/binance/btc/Binance_BTCUSDT_1h.csv"
        btcData = bdp.BinanceNoOfficialDataProvider(sourceFile)
        print(btcData.data)
        btcData.mocked_corrector()
        print(btcData.data)
    """
