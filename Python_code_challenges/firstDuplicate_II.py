
""" firstDuplicateII 
Given an array of integers, create a function that returns the index 
(0-based) of the first integer which does have a duplicate on the 
array (start by the index 0 on the array). Return -1 if no duplicate is 
found.
"""

def firstDupli(arr):    
    dicArr, result = {}, set()
    for i, ele in enumerate(arr):
        if ele in dicArr: result.add(dicArr[ele])
        else: dicArr[ele] = i
    if result: return sorted(result)[0]
    return -1

print(firstDupli([1, 3, 5, 6, 2, 1, 8, 1, 2])) # 0
print(firstDupli([3, 5, 5, 1, 6, 3])) # 0 
print(firstDupli([11, 3, 5, 6, 2, 12, 8, 9, 2])) # 4
print(firstDupli([1, 3, 5, 6, 2, 12, 8, 21])) # -1
print(firstDupli([1, 3, 5, 6, 2, -2])) # -1
print(firstDupli([])) # -1
