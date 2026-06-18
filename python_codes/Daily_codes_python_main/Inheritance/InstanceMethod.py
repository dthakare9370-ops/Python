
class Demo:
    
    a = 10
   
    
    def instanceMethod(self):
        self.b = 20
        print("Instance Method")
        print("a : ",a)
        print("b : ",self.b)

    @classmethod
    def classMethod(cls):
        print("Class Method")

    @staticmethod
    def staticMethod():
        print("Static Method")

obj = Demo()
obj.instanceMethod()
obj.classMethod()
Demo.classMethod()

Demo.staticMethod()
