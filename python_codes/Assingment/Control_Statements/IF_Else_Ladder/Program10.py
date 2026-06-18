
no1 = int(input('Enter three angle : '))
no2 = int(input())
no3 = int(input())

sums = no1+no2+no3
if sums>180 or no1<=0 or no2<=0 or no3<=0:
    print("Invalide Triangle")
elif no1<90 and no2<90 and no3<90:
    print('Acute Triangle')
elif no1>90 and no2>90 and no3>90:
    print('Obtuse Triangle')

