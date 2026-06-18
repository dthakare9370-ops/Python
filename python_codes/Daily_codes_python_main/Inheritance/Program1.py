
class Demo:
        
    def __init__(self):
        print("Demo Constructor")

    def __new__(cls,*args,**kwargs):
        print("memory Allocation - Demo Class ")
        return super().__new__(cls)

#obj = Demo()
obj = Demo.__new__(Demo)

print(obj)
Demo.__init__(obj)


'''print(obj)
print(Demo)
print(Demo.__dict__)

'''
