
age = int(input('Enter the Age : '))
weight = int(input('Enter the Weight : '))
hb = float(input('Enter the hb : '))

if age>=18 and age<=65:
    if weight<=50:
        if hb<=12.5:
            print("Eligibility for Blood Donation")
        else:
            print("not Eligibility for Blood Donation")
    else:
        print("not Eligibility for Blood Donation")
else:
            print("not Eligibility for Blood Donation")
