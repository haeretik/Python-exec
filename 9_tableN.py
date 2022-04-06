#!/usr/bin/env python

# Get number from the user, and display table for that number

number = int(input(f"Enter number: "))

print(f"Table of {number}")

for i in range(1,11) :
    print(f"{i} x {number} = {i * number}")
