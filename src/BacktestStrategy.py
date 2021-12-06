import Strategy
import abc

class BacktestStrategy(Strategy, metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__()

    @abc.abstractclassmethod
    def getNextCandle()

