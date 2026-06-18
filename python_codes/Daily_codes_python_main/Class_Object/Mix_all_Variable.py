
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
        

obj = Demo()
print(obj.x)
print(Demo.x)

Demo.instanceMethod(obj)
print(globals())
print(obj)
