
class Demo:
    a=10
    b=20

    def instanceMethod(self):
        print("Instance Method")

    @classmethod
    def classMethod(cls):
        print("class Method")

    @staticmethod
    def staticMethod():
        print("Static Method")

obj = Demo()

obj.instanceMethod()
Demo.classMethod()
obj.staticMethod()
