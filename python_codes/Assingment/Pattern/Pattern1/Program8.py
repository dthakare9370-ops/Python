

row = int(input("Enter the Row : "))


for i in range(1,row+1):
    no = 1
    for j in range(1,i):
        print(end="\t")

    for k in range(1,row-i+2):
        print(no,end="\t")
        no += 1

    print()
