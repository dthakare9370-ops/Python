

def fun(*args,**kwargs):
    

    
    for i in args:
        a = i
    print("Fun A : ",a)
    b = kwargs.get('b')
    c = kwargs.get('c')
    print("B : ",b)
    print("C : ",c)



    '''def run():
        print("Run A : ",a)
    
    return run
'''


obj = fun(10,b=40,c=60)
#obj()   

