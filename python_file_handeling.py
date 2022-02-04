# open file and read file
f = open('new.txt','r')
print(f.read())

#  read by specified text
f = open('new.txt','r')
print(f.read(7))

# print one line only
f = open('new.txt','r')
print(f.readline())

# print first two lines
f = open('new.txt','r')
print(f.readline(),end="")
print(f.readline())

# print file content with loop
files = open('new.txt','r')
for i in files:
    print(i,end="")

# close file
f = open('new.txt','r')
print(f.read())
f.close()

# append data
f = open('new.txt','a')
f.write("\nThis is new line in text file")
f.close()
print('data added ')

# add data and open file again
f = open('new.txt','a')
f.write("\nThis new line in file ")
f.close()
f = open('new.txt','r')
print(f.read())

# overwrite file content
f = open('new.txt', 'w')
f.write("This is override all content")
f.close()
f = open('new.txt', 'r')
print(f.read())

# create new file
# f = open('one.txt','x')

# create new file
# f = open('two.txt', 'w')
# print('file created')

# delete file
# import os
#
# os.remove('two.txt')
# print("file removed")


# check file exits or not
import os

if os.path.exists('two.txt'):
    os.remove('two.txt')
else:
    print("file not exist")

# delete folder
import  os
os.rmdir('demo')
print("folder deleted")
