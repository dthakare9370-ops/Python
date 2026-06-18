
def checkVoting(age):
    if age>=18:
        print('Eligible for Voting ')
    else:
        print("Not Eligible for Voting ")

age = int(input('Enter the Age : '))
checkVoting(age)
