no = int(input('Enter the Number : '))

if no>0 and no%2==0:
    print('Positive Even')
elif no<0 and no%2==0:
    print('Negative Even')
elif no>0 and no%2!=0:
    print('Positive Odd')
else:
    print('Negative Odd')
