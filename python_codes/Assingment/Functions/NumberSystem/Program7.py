def neonNumber(no):
    sum = 0;
    no = temp
    while(no>0):
        rem = no%10
        sum += rem
        no//=10
    if(temp==sum):
        print("Neon Number")
    else:
        print("Not Neon Number")

no = int(input("Enter Number : "))
neonNumber(no);
