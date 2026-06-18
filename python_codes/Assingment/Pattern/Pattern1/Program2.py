

row = int(input("Enter the Row : "))

for i in range(1,row+1):
    no=1
    for j in range(1,row+1):
        print(no,end=" ")
        no += 2
    print()
