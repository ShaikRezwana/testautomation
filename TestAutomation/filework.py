#read data from file
#obj=open("D:\py.txt",'r')
#read all data from the file
#print(obj.read())

#read only one line from file
#print(obj.readline())
#print(obj.readline())

#read only few characters from file by passing no on characters
#print(obj.read(10))

#program 1: read all characters from the file and display 1 by 1

'''obj=open("D:\py.txt",'r')
#for i in obj.read():
#   print(i)


#program 2: read all data line by line
s=obj.readline()
while(s):
    print(s)
    s=obj.readline()'''

#write data to the file(remove previous data and add new data)
'''obj=open("D:\py1.txt",'w')
obj.write("i am python programming")
obj.close()'''
# apppend: keeps original data and adds new data to it'
obj=open("D:\py1.txt",'a')
obj.write("i am new data of python programming")
obj.close()

