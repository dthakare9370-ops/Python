

row = int(input("Enter the Row : "))


for i in range(1,row+1):
    no = row-i+1
    for j in range(1,row-i+2):
        print(no,end=" ")
        
    print()
