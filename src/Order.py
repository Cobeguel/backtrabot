from enum import Enum


class OrderType(Enum):
    # Indicates if the order is buy or sell
    Long=0
    Short=1

class OrderTypeMarket(Enum):
    Limited=0
    Market=1
    OCO=2

class Order:
    def __init__(self, id, orderType, orderTypeMarket, asset, quantity, entryPrice = -1):
        self.id = id
        self.orderType = orderType
        self.orderTypeMarket = orderTypeMarket
        self.asset = asset
        self.quantity = quantity
        self.entryPrice = entryPrice


        
