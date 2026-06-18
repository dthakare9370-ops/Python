
from abc import ABCMeta,abstractmethod

class Demo(metaclass = ABCMeta):

    #@abstractmethod
    def marry(self):
        pass

obj = Demo()

print(type(Demo))
