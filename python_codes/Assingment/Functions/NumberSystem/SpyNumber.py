def SpyNumber(no):
    pro = 1
    sum = 0
    while(no>0):
        rem = no%10
        sum = sum+rem
        pro = pro*rem
        no//=10
    
    if(pro==sum):
        print("spy Number")
    else:
        print("not spy Number")

no = int(input("Enter Number : "))
SpyNumber(no)
