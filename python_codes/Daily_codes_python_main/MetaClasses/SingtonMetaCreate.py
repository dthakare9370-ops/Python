

class SingletonMeta(type):
    
    instance = None

    def __call__(cls,*args,**kwargs):
    
        if cls.instance is None:
            cls.instance = super().__call__(*args,**kwargs)
        return cls.instance

class Demo(metaclass = SingletonMeta):

    def __init__(self):
        print("Demo Constructor")

    def __new__(cls,*args,**kwargs):
        print("Memmory Allocation - Demo")
        return super().__new__(cls)

class DemoChild(Demo):

    def __init__(self):
        print("DemoChild Constructor")

    def __new__(cls,*args,**kwargs):
        print("Memory allocation - DemoChild")
        return super().__new__(cls)


obj1 = DemoChild()
obj2 = DemoChild()
print(obj1)
print(obj2)


