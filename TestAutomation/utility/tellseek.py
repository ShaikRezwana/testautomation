#Tell: tells current cursor position of the file
obj=open("D:\py1.txt",'r')
'''print(obj.tell())
print(obj.readline())
print(obj.tell())'''

#seek:navigate our cursor position to the diff location
obj.seek(5)
print(obj.tell())