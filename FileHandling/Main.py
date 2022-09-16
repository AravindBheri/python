file = open('FileHandling\Mydata', 'r')
print(file.read())

newfile = open('FileHandling//Newdata', 'w')
for data in file:
    newfile.write(data)



