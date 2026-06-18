

row = int(input("Enter the Number of Row : "))
no=(row*(row+1));
for i in range(1,row+1):
    for j in range(1,row-i+2):
        print(no,end="\t")
        no = no - 2
    print()
