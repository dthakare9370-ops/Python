
per = int(input('Enter Percentage : '))
examSc = int(input('Enter Exam Score : '))

if per>=90 and examSc>=90:
    print("Elite Program")
elif per>=80 and examSc>=70:
    print("Standard Program")
elif per>=60 and examSc>=50:
    print('Basic Program')
else :
    print("Not Eligible")
