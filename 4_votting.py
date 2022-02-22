#!/usr/bin/env python

# get age from the user
# get name from the user

name =  input(f"Enter your name: ")
age = int(input(f"Enter your age: "))
#print(type(age))
if(age>=18):
    print(f"Hi {name} You can take part in votting")
else:
    print(f"Sorry, you cannot take part because your age is {str(age)} year, you will be able to participate after {str(18-age)} year")

