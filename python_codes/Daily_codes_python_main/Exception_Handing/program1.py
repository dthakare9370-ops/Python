
print("Start Code")

try:
    x = int(input("Enter number 1 : "))
    y = int(input("Enter Number 2 : "))
    result = x/y
    print(result)
finally:
    print("Finaly Block 1")
except ValueError:
    print("Invalide Enter Value")
except ZeroDivisionError:
    print("Divide By Zero Error")
except Exception:
    print("Kahipan Yeude")
finally:
    print("Finaly Block 2")

print("End Code")
