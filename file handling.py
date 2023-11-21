# file handling
#text file,pdf files,images,audio,video
#types of mode
#r- read
#w- write
#a- append
#w+ - writing and read 
#r+ - read and writing
#a+ - appending
#x - exclusive

#write
file= open("/Users/GOWTHAMRAJ/Desktop/Python new/file.txt", 'w')
file.write("I am working in Aspire system\n")
file.write('It is located in chennai\n')
branch=['siruseri\n','U.S\n','Hydrabad\n','Kochi\n']
file.writelines(branch)
print(file.name)
print(file.mode)
print("Readability",file.readable())
print('writability',file.writable())
print('file opened or closed',file.closed)
file.close()
print('file opened or closed',file.closed)

print('..............................................')

#read
files=open("/Users/GOWTHAMRAJ/Desktop/Python new/file.txt",'r')
# content=files.read()
# print(content)
#print(files.readlines())
#print(files.read(10))
conn=files.readlines()
for line in conn:
    print(line,end=' ')
    print(type(line))
files.close()

import os,sys
filename=input("Enter your file name ")
if os.path.isfile(filename):
    print('file is present')
    file=open(filename,'r')
    linecount=0
    for line in file:
        print(line)
        linecount=linecount+1
    print(linecount)

else:
    print('file is not present')

print('............................................')

#binarydata
#copy pate image
inputfile=open("/Users/GOWTHAMRAJ/Downloads/GOWTHAMRAJ_PHOTO.jpg",'rb')
output=open("/Users/GOWTHAMRAJ/Downloads/GOWTHAMRAJ.jpeg",'wb')
byte=inputfile.read()
output.write(byte)

print('..........................................')

#CSV -comma seperated values

import csv
with open("student.csv",'w',newline='') as file:
    obj=csv.writer(file)#writer object
    obj.writerow(['Student_ID','Student_name','Student_address'])
    count=int(input('Enter no of student'))
    for i in range(count):
        sid=int(input('Enter studentid '))
        sname=input('Enter student name ')
        saddress=input('Enter student address')
        obj.writerow([sid,sname,saddress])

print('............................................')


with open("student.csv",'r',newline='') as file:
    objread=csv.reader(file)#reader object
    for line in objread:
        for eachword in line:
            print(eachword,end='')
        print()
    
