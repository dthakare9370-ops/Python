

'''
def isPerfectNo(no):
    sum = 0;
    for i in range(1,int(no/2)+1):
        if no%i==0:
            sum = sum + i
    return sum
'''

def isPerfectNo(no):
    sum = 0
    i=1
    while(i<=int(no/2)):
        if no%i==0:
            sum = sum + i
        i = i+1
    return sum


no = int(input('Enter the number : '))
print(isPerfectNo(no))
if isPerfectNo(no)==no:
    print("Number is Perfect Number ")
else:
  print("Number is Not Perfect Number ")

