
""" deviation
Given an array of integer elements and an integer d please consider all 
the sequences of d consecutive elements in the array. For each sequence 
we compute the difference between the maximum and the minimum value of 
the elements in that sequence and name it the deviation.

Your task is to

write a function that computes the maximum value among the deviations of 
all the sequences considered above
print the value the standard output (stdout)

Note that your function will receive the following arguments:

v
    which is the array of integers
d
    which is an integer value giving the length of the sequences

Data constraints

the array will contain up to 100,000 elements
all the elements in the array are integer numbers in the following range: 
[1, 2^31 -1]
the value of d will not exceed the length of the given array

Efficiency constraints

your function is expected to print the result in less than 2 seconds

Example Input              Output

v: 6, 9, 4, 7, 4, 1        6
d: 3 
"""

def deviation(v, d):
    drop, maxD, tMax, tMin = 0, float('-inf'), float('-inf'), float('inf')
    for i in range(len(v)-d+1):
        if tMin < drop < tMax and tMin <= v[i+d-1] <= tMax: continue
        tMax, tMin, drop = max(v[i:i+d]), min(v[i:i+d]), v[i]
        maxD = max(maxD, (tMax-tMin))
    print(maxD)

""" brute force, slower
def deviation(v, d):
    maxD = float('-inf')
    for i in range(len(v)-d+1):
        maxD = max(maxD, (max(v[i:i+d])-min(v[i:i+d])))
    print(maxD)
"""

""" alternative, longer, slower
def deviation(v, d):
    minSli, maxSli = [], []
    for n in v[:d]:
        while len(minSli) != 0 and minSli[-1] > n:
            minSli.pop()
        minSli.append(n)
        while len(maxSli) != 0 and maxSli[-1] < n:
            maxSli.pop()
        maxSli.append(n)
    maxD = maxSli[0] - minSli[0]
    for index in range(d, len(v)):
        tmpN, drop = v[index], v[index-d]
        if maxSli[0] == drop: maxSli.remove(drop)
        if minSli[0] == drop: minSli.remove(drop)
        while len(minSli) != 0 and minSli[-1] > tmpN:
            minSli.pop()
        minSli.append(tmpN)
        while len(maxSli) != 0 and maxSli[-1] < tmpN:
            maxSli.pop()
        maxSli.append(tmpN)
        maxD = max(maxD, (maxSli[0]-minSli[0]))
    print(maxD)
"""

deviation([6, 9, 4, 7, 4, 1], 3) #6
deviation([6, 9, 4, 7, 4, 1], 6) #8
deviation([6, 9, 4, 7, 4, 1, 4, 5, 1, 2], 3) #6
deviation([1, 2, 3, 4, 5, 6], 2) #1
deviation([6, 9, 4, 9, 4, 7, 7, 4, 1], 3) #6
deviation([1], 1) #0

""" test module (big numbers)
import time
import random
def testF():
    count = 1
    random.seed()
    for i in range(count):
        test = random.sample(range(10000000), 1000000)
        testlen = random.randint(2,50)
        start = time.time()
        deviation(test, testlen)
        end = time.time()
        print('last result time in seconds:', end - start)
testF()
"""
