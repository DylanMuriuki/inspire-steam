#Name:Dylan Muriuki
#Date:24/02/2026
#Program to perform file operations

#create new file
new_file = open("student_data.txt", "r+")

#write to new file
new_file = open("student_data.txt", "r+")
new_file.write("{ Student Name : Bob Afwata , ID : 20003230 , Email : bafwata32@gmail.com }")

#read from the file
data = new_file.read()

print(data)
new_file.close

#delete file
#Use os module
import os
#os.rmdir("folder")

