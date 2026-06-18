


print("Start code")

def voting(age):
    if age < 18:
        raise ValueError("Not Eligible For Voting")
    else:
        print("Eligible")


age = int(input("Enter the age : "))

try:
    voting(age)
except ValueError as e:
    print(type(e).__name__," : ",e) 
