
""" minimumLengthUniqueWindow
Given an array "arr" of characters, create a function that returns a list 
of integers representing the length of all consecutive "windows" of characters 
in the array which only contain characters that are not present in any 
other window. All windows must have the minimum size possible.  

For example:
 
arr = [j, k, r]

Output = [1, 1, 1]

Explanation: because there are no recurring characters, all windows can be 
have the minimum length of 1.

Another example:

arr = [r, b, n, r]

Output = [4]

Explanation: because 'r' appears more than once, everything between the 
first and last appearance of 'r' must be in the same window.

Another example:

arr = [z, b, c, d, z, e, f, g, h, i, j, e]

Output = [5, 7]
"""

def createWin(arr):
    dic, res, start, end, count = {}, [], 0, -1, 1
    for idx, ele in enumerate(arr):
        if ele in dic: dic[ele].append(idx)
        else: dic[ele] = [idx]
    while start < len(arr):
        if start == end:
            res.append(count)
            start += 1
            end, count = -1, 1
        elif end == -1 and len(dic[arr[start]]) == 1:
            start += 1
            count = 1
            res.append(1)
        elif end == -1:
            end = dic[arr[start]][-1]
            start += 1
            count += 1
        else:
            if dic[arr[start]][-1] > end:
                end = dic[arr[start]][-1]
            start += 1
            count += 1
    return res
        

print(createWin(['j', 'k', 'r'])) # [1, 1, 1] 
print(createWin(['r', 'b', 'n', 'r'])) # [4] 
print(createWin(['z', 'b', 'z', 'b', 'c', 'b', 'z', 'c', 'z', 'd', 'e', 
'f', 'e', 'g', 'd', 'e', 'h', 'i', 'j', 'h', 'k', 'l', 'i', 'j'])) # [9, 7, 8]
print(createWin(['z', 'b', 'c', 'd', 'z', 'e', 'f', 'g', 'h', 'i', 'j', 'e']))
# [5, 7]
print(createWin(['z', 'z', 'c', 'b', 'z', 'c', 'h', 'f', 'i', 'h', 'i']))
# [6, 5]
print(createWin(['p', 'b', 'c', 'd', 'e', 'd', 'z', 'd', 'r', 'n', 't', 'n'])) 
# [1, 1, 1, 5, 1, 3] 
