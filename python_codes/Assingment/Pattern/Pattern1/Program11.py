

row = int(input("Enter the Row : "))


for i in range(1,row+1):
    no = row
    for j in range(1,row-i+1):
        print(end="\t")

    for k in range(1,i+1):
        print(no,end="\t")
        no -= 1

    print()
