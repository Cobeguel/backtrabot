import abc

class A(metaclass=abc.ABCMeta):
    def __init__(self, value):
        self.value = value

    @abc.abstractclassmethod
    def increment(self):
        pass

class B(A):
    def __init__(self, value):
        super().__init__(value)

    def increment(self):
        self.value+=1


if __name__ == "__main__":
    var = B(0)
    var.increment()
    print(var.value)
    print(type(var))
    print(type(var.increment))
    print(type(var.value))