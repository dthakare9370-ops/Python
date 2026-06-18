
def Prod(no):
    product = 1
    i=1
    while i<=no:
        product = product*i;
        i= i+1
    return product

no = int(input('Enter the Number : '))
print("Product of ",no," : ",Prod(no))

