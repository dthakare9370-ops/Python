def countDigit(no):
    while(no>0):
        rem = no%10
        if rem%2!=0:
            print(rem**2,end=" ")
        else:
            print(rem,end=" ")
        
        no//=10

no = int(input("Enter Number : "))
countDigit(no);
