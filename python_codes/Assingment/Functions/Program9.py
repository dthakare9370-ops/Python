
def printData(*args):
    sum=0
    for i in args:
        sum = sum + i
    avg = sum/len(args)
    print(avg)

printData(10,20,30,40)
