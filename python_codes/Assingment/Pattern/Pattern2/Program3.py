

row = int(input("Enter the Number of Row : "))
for i in range(1,row+1):
    no = row-i+1
    for j in range(1,i+1):
        print(no,end="\t")
        no = no + (row-i+1)
    print()
