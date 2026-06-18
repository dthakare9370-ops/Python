def sumOfDigit(no):
    sum=0;
    while(no>0):
        rem = no%10
        if(rem%2==0):
            sum+=rem;
        no//=10
    return sum

no = int(input("Enter Number : "))
print(sumOfDigit(no))
