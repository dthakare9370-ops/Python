
def fact(no):
    fact = 1;
    if(no==0):
        return no
    else:
        while no>0:
            fact = fact*no
            no = no-1
        return fact

no = int(input('Enter the Number : '))
print(fact(no))
