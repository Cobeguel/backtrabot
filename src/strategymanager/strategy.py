import abc

class Strategy(metaclass=abc.ABCMeta):
    def __init__(self):
        self.deals=[]


    @abc.abstractclassmethod
    def start(self):
        pass

    @abc.abstractclassmethod
    def pause(self):
        pass

    @abc.abstractclassmethod
    def buy():
        pass

    @abc.abstractclassmethod
    def sell():
        pass

    