
""" greatestCommonDivisor
The greatest common divisor (GCD) of n numbers is the largest positive 
integer that divides all the numbers without giving a remainder.

Write an algorithm to determine the GCD of n positive integers. Your inputs 
are an array of integers 'arr' which is guaranteed to have at least one 
value, and an integer 'n', being that 0 < n <= len(arr). 
""" 

def findGCD(n, arr):
    count, store = 0, 0
    sArr = sorted(arr)
    for i in range(1, sArr[0]+1):
        for num in sArr[:n]:
            if num % i == 0: count += 1
            if count == n:
                store = i
                count = 0
        count = 0
    return store


print(findGCD(5, [2, 3, 4, 5, 6, 7, 8, 9])) # 1
print(findGCD(2, [4, 9, 17, 11, 9, 8, 10])) # 4
print(findGCD(5, [2, 6, 8, 10, 14])) # 2
print(findGCD(6, [12, 14, 6, 8, 10, 2])) # 2
print(findGCD(5, [2, 2, 2, 2, 2, 2, 4, 6, 8, 10])) # 2
print(findGCD(5, [2, 2, 2, 2, 2, 4, 6, 8, 10, 2])) # 2
print(findGCD(11, [2, 2, 2, 2, 2, 2, 4, 6, 8, 10, 7])) # 1

