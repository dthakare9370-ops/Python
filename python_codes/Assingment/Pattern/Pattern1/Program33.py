

row = int(input("Enter the Row : "))
no=1
for i in range(1,row+1):
    
    for j in range(1,row+1):
        print(no,end=" ")
        no += 2
        
    print()
    no=row*i+1
