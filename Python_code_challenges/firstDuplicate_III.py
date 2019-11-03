
""" firstDuplicateIII
Given an array of integers, create a function that returns the index 
(0-based) of the first integer which has already appeared once on the array 
(starting from the index 0 of the array). Return -1 if no duplicate is 
found.
"""

def firstDupli(arr):    
    setArr = set()
    for i, ele in enumerate(arr):
        if ele in setArr: return i
        else: setArr.add(ele)
    return -1
        

print(firstDupli([1, 3, 5, 6, 2, 1, 8, 1, 2])) # 5
print(firstDupli([3, 5, 5, 1, 6, 3])) # 2
print(firstDupli([11, 3, 5, 6, 2, 12, 8, 9, 2])) # 8
print(firstDupli([1, 3, 5, 6, 2, 12, 8, 21])) # -1
print(firstDupli([1, 3, 5, 6, 2, -2])) # -1
print(firstDupli([])) # -1

