# num = 64

# sqr = num ** (1/2)

# print("The Squre root of Given number is\t ",sqr)

import math


# num = int(input("Enter a number here\t"))
# sqr =math.sqrt(num)
# print("The squrare root of Given number is\t ",sqr)
   
import math

def find_sqr_num(num):
    sqr = math.sqrt(num)
    return sqr

num = int(input("Enter a Number\t "))

sqr = find_sqr_num(num)
print(sqr)