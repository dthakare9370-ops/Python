

fileObj = open("Ganesh.txt","a+")

#data = fileObj.read()

#print(data)


fileObj.write("Hello")

fileObj.seek(0)

data = fileObj.read()

print(data)

fileObj.close()
