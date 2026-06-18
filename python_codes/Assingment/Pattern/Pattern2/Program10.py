

row = int(input("Enter the Number of Row : "))
no=row
for i in range(1,row+1):
    for j in range(1,i):
        print(end="\t")

    for j in range(1,row-i+2):
        print(no**2,end="\t")
        no+=2
    print()
