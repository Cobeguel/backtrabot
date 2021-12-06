import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime
import time
import abc

def unix_time_to_s(t):
    now = time.mktime(time.gmtime())
    if t > now:
        t=t/1000.0
    return t


class OHLC:
    def __init__(self, open, high, close, low, volume = 0.0):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume


class DataProvider(metaclass=abc.ABCMeta):
    def __init__(self, dataSource):
        self.dataSource = dataSource



