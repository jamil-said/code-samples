
""" perfectSquareRange
Task: given a range of numbers, count the number of perfect squares
where the square root is a whole number.
const A = 250
const B = -300
"""

#not tested on large test case
def squares(a, b):
    count = 0
    if a < 0 and b < 0: return 0
    elif a >= 0 and b < 0: rng1, rng2 = 0, a
    elif a < 0 and b >= 0: rng1, rng2 = 0, b
    elif a >= 0 and b >= 0:
        if a >= b: rng1, rng2 = b, a
        else: rng1, rng2 = a, b
    sq1, sq2 = int(rng1**(1/2)), int(rng2**(1/2)+1)
    for i in range(sq1, sq2):
        if rng1 <= (i**2) <= rng2: count += 1
    return count

print(squares(250, -300)) #16
print(squares(250, 200)) #1
print(squares(9, 25)) #3


""" alternative, brute force, much slower
def squares(a, b):
    count = 0
    if a < 0 and b < 0: return 0
    elif a >= 0 and b < 0: rng1, rng2 = 0, a
    elif a < 0 and b >= 0: rng1, rng2 = 0, b
    elif a >= 0 and b >= 0 and a >= b: rng1, rng2 = b, a
    elif a >= 0 and b >= 0 and a < b: rng1, rng2 = a, b
    for i in range(rng1, rng2):
        if (i**(1/2)).is_integer(): count += 1
    return count
"""
