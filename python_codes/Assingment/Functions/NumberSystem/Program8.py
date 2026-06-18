def reverseNumber(no):
    temp = no
    rev = 0;
    while(no>0):
        rem = no%10
        rev = rev*10+rem
        no//=10
    if(temp==rev):
        print("palindrom Number")
    else:
        print("Not Palindrom")

no = int(input("Enter Number : "))
reverseNumber(no);
