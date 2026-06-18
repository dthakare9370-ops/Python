

no1 = int(input('Enter First number : '))
no2 = int(input('Enter Second number : '))
no3 = int(input('Enter Third number : '))

ls = [no1,no2,no3]
ls.sort();

no1 , no2, no3 = ls

if no3 * no3 == no1 * no1 + no2 * no2:
    print('It is Right Angle Triangle')
else:
    print('Is is not Right Angle Triangle')
