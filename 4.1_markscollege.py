#!/usr/bin/env python

# get age from the user
# get marks from the user

name =  input(f"Enter your name: ")
marks = int(input(f"Enter your marks: "))

if(marks>=60):
    print(f"Hi {name}, welcome!")
else:
    print(f"Sorry! {name}, you cannot take admission, you need {str(60-marks)} numbers more to take admission")

