def StrongNumber(no):
    sum = 0
    temp = no
    
    while temp>0:
        rem = temp%10
        fact=1
        for i in range(1,rem+1):
            fact = fact*i

        sum = sum+fact;
        temp//=10

    if(sum==no):
        print('Strong Number')
    else:
        print("Not Strong number")


no = int(input("Enter Number : "))
StrongNumber(no)
