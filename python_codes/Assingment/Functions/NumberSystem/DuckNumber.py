def DuckNumber(no):
    noStr = str(no)

    if(noStr[0] == 0):
        print(no," is  Not Duck Number")
    
    if '0' in noStr:
        print(no," is Duck Number")
    else:
        print(no," is  Not Duck Number")


no = int(input("Enter Number : "))
DuckNumber(no)
