def countDigit(no):
    count=0;
    while(no>0):
        count+=1;
        no//=10
    print(count)

no = int(input("Enter Number : "))
countDigit(no);
