def armStrongNumber(no):
    sum = 0
    temp = no
    count=0
    while temp>0:
        count+=1
        temp//=10

    temp=no
    
    while temp>0:
        rem = temp%10
        ans = rem**count
        sum = sum+ans
        temp//=10

    if(sum==no):
        print('ArmStrong Number')
    else:
        print("Not ArmStrong number")


no = int(input("Enter Number : "))
armStrongNumber(no)
