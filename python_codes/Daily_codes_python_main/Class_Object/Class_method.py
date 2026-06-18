
class Demo:

    x = 10
    y = 20
    def __init__(self):
        print("Demo Constructor")
        self.a = 30

    def instanceMethod(self):
        print(self)
        print(self.__dict__)
        print(self.a)
        print(self.__class__.x)
    
    @classmethod
    def clsMethod(cls):
        print("class Method")
        print(cls.x)
        print(cls.__dict__)
       
    def staticMethod():
        print('Static method')
        
        

Demo.staticMethod()
print(Demo.__dict__)
