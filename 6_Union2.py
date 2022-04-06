#!/usr/bin/env python

# print a union of two

a = {3,2,4,5,6,7,8}
b = {4,12,5,1,6,8}

#c = {13,14,15}
#d = a.union(b,c)

c = a.difference(b)

print(f"We are finding UNION of two")
print(f"{c}")
