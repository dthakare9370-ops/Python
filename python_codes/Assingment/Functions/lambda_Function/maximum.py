
#maxNumber = lambda x,y : max(x,y) 

maxNumber = lambda a,b : a if a>b else b

no1 = int(input("Enter the Number 1 : "))
no2 = int(input("Enter the Number 2 : "))

print(maxNumber(no1,no2))
