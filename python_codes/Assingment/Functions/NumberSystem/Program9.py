
def deficientNumber(no):
    sum = 0 
    for i in range (1,no//2+1):
        if(no%i==0):
            sum = sum +i;

    if(sum<no):
        print("Deficient Number ");
    else:
        print("Not Deficient Number");


no = int(input("Enter Number : "))
deficientNumber(no);
