
class BiryaniSamplyException(Exception):
    pass

class Order:


    BiryaniCount = 1

    def __init__(self):
        print("Order Cnstructor")
    
    def getBiryani(self):

        if self.BiryaniCount == 0:
            raise BiryaniSamplyException("Ghari Ja ....")
        else:
            print("Serving......")
            self.BiryaniCount -= 1

obj = Order()
try:
    obj.getBiryani()
    obj.getBiryani()
except Exception as e:
    print(type(e).__name__," : ",e)
