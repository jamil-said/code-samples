""" integerToHexConversion
Convert an integer number into hex. Hex numbers may be signed (Ex: int -26 = hex -1a). Return all hex letters 
in lowercase. Do NOT use the built-in function hex() or the 2 complement method to solve this problem.
"""


def convert(n):
    res = '' if n else '0'
    s = 1 if n < 0 else 0
    n = abs(n)
    while n != 0:
        temp = 0
        temp = n % 16
        res = (res+chr(temp+48)) if temp <10 else (res+chr(temp + 87)) #55 for capital
        n = int(n / 16)
    return res[::-1] if not s else '-' + res[::-1]
    

print(convert(26)) #1a
print(convert(72)) #48
print(convert(4329)) #10e9
print(convert(0)) # 0
print(convert(-26)) # -1a
print(convert(-4329)) #-10e9

