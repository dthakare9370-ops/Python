
x = 10

def fun():
    
    x = 20 

    def run():
        global x
        
        print(x)
    return run 

obj = fun()
obj()
