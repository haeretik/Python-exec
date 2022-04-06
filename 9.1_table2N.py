#!/usr/bin/env python
# Get 2 numbers from the user, and display table for thats number

num1= int (input(f"Introduce number 1: "))
num2= int (input(f"Introduce number 2: "))

for i in range(1,11):
    print(f"{i} x {num1} = {i * num1}")

print(f"")

for i in range(1,11):
    print(f"{i} x {num2} = {i * num2}")