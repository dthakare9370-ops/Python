

print("Start Code")
print("Connection is Firebase/Network")

try:
    x = int(input("Enter the Number 1 : "))
    y = int(input("Enter the Number 2 : "))
    result = x/y
except ValueError:
    print("Wrong Input Format")
except ZeroDivisionError:
    print("Divide by Zero Error ")
else:
    print("Result : ",result)
finally:
    print("Connection Close ")

print("End Code")
