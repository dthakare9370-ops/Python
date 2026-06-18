
amt = int(input('Enter the Amount : '))

if amt>=1000 and amt<=4999:
    print('Discount Price : 5%');
    dic=amt*5/100
    amt = amt-dic;
    print("Final Price : ",amt)
elif amt>=5000 and amt<=9999:
    print('Discount Price : 10%');
    dic=amt*10/100
    amt = amt-dic;
    print("Final Price : ",amt)
elif amt>=10000 and amt<=19999:
    print('Discount Price : 20%');
    dic=amt*20/100
    amt = amt-dic;
    print("Final Price : ",amt)
else:
    print('Discount Price : 30%');
    dic=amt*30/100
    amt = amt-dic;
    print("Final Price : ",amt)
