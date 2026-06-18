

#fileObj = open("Ganesh.txt",'r')
#fileObj.close()


with open("Ganesh.txt",'r+') as fileObj:
    data = fileObj.readline()
    print(data)
