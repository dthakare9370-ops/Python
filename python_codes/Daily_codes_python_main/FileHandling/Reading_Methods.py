
fileObj = open("Ganesh.txt","r")


data = fileObj.read()
print(data)

fileObj.seek(0)

data = fileObj.readline()
print(data)

fileObj.seek(0)

data = fileObj.readlines()
print(data)

fileObj.close()
