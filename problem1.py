#!/usr/bin/env python

num= int (input("Numer of Iteracions?"))
print(f"Number\t\tSquare\t\tCube")

for n in range(num+1):
    print(f"{n}\t\t{n*n}\t\t{pow(n,3)}")
    n+=1


#print("Number \t\t Square")
#print("1 \t\t "+str(1*1))
#print("2 \t\t "+str(2*2))
#print("3 \t\t "+str(3*3))
#print("4 \t\t "+str(4*4))
#print("5 \t\t "+str(5*5))
