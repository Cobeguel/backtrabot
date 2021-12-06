import abc
from enum import Enum, auto


"""
Le damos el valor de enumerado el mismo nombre para que cuando los reciba la condición
lo pueda hacer mediante un diccionario cuyas llaves deben coincidir con el valor
del enumerado. Movida, que haya dos RSI, para resolver esto lo que hacemos es
agruparlos por listas -> NO
"""
class IndicatorType(Enum):
    empty="empty"
    rsi="rsi"

class ConditionIndicator(metaclass=abc.ABCMeta):
    def __init__(self):
        
    @abc.abstractclassmethod
    def get():
        pass


class Condition(metaclass=abc.ABCMeta):
    def __init__(self):
        self.indicator = []

    @abc.abstractclassmethod
    def isConditionTrue(self, paramList):
        pass

