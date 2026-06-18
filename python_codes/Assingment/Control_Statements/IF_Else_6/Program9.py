ch1 = input('Enter First Char : ')
ch2 = input('Enter Second Char : ')

if ord(ch1)%2!=0 and ord(ch2)%2!=0:
    sum = ord(ch1) + ord(ch2)
    print(sum)
else:
    print("Sum is Even")
