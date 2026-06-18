
fileObj = open("Ganesh.txt","w+")


data = fileObj.read()
print(data)

fileObj.write("Ganesh")

fileObj.seek(0)

data = fileObj.read()
print(data)

fileObj.writelines(["How\n","Are\n","You\n"])

fileObj.seek(0)

data = fileObj.read()
print(data)

fileObj.close()
