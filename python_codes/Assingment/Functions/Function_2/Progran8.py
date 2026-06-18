

def prime(no):
    if(no==1 or no==0):
        return False
    else:
        i=2
        while(i<no):
            if no%i==0:
                return False
            i = i+1
        return True

no = int(input('Enter the Number : '))
if prime(no):
    print("Number is Prime Number ")
else:
    print("Number is not Prime Number ")
