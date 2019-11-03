
""" squareRoot
Given a positive float number n and a integer precision number p, find the 
square root of n with p digits precision (rounded to the p digit) without 
using exponentiation or square root calculations and/or libraries. 

Example: 
findSquare(50, 6) = 7.071068
"""

def findS(n, p):
    prec = 1/int('1'+'0'*p)
    x, y = n, 1
    while (x-y) > prec:
        x = (x+y)/2
        y = n/x
    return round(x, p)

print(findS(50, 6)) # 7.071068
print(findS(51, 6)) # 7.141429
print(findS(51.8, 7)) # 7.1972217
print(findS(53.7, 2)) # 7.33

