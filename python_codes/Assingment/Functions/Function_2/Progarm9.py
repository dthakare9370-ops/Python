

def comNumber(no):
    i=1
    count=0

    while(i<=no):
        if no%i==0:
            count= count+1
        i = i+1
    return count

no = int(input('Enter the Number : '))
if comNumber(no)>2:
    print('Number is Composite numebr ')
else:
    print('number is Nor Composite Number ')
