
def avg(*marks):
    sum = 0
    for i in marks:
        sum = sum + i
    avg = sum/len(marks)
    return avg

print(avg(10,20,30,40,50))
