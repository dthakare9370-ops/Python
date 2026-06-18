
def decorCoffee(func):

    def wapper():
        coffee = func();
        extra = input("do your want to add Extra Detail : (Sugar, Milk Type)")

        print("Coffee Type : ",coffee)

        if(extra==''):
            print("No Extra add")
        else:
            print("Extra add : ",extra)
    return wapper



@decorCoffee
def orderCoffee():
    cfType = input("Enter the Type of Coffee (Mocha)")
    return cfType


orderCoffee()
