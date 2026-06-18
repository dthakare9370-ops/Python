

row = int(input("Enter the Number of Row : "))
no=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(no,end="\t")
        no = no + 1
    print()
    no-=1
