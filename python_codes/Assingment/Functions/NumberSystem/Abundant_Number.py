
def abundantNumber(no):
    sum = 0 
    for i in range (1,no):
        if(no%i==0):
            sum = sum +i;

    if(sum>no):
        print("Abundant Number ");
    else:
        print("Not Abundant Number");


no = int(input("Enter Number : "))
abundantNumber(no);
