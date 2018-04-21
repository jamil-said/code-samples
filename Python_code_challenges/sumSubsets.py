
""" sumSubsets -- 30min.
Given a sorted array of integers arr and an integer num, find all possible 
unique subsets of arr that add up to num. Both the array of subsets and 
the subsets themselves should be sorted in lexicographical order.

Example

For arr = [1, 2, 3, 4, 5] and num = 5, the output should be
sumSubsets(arr, num) = [[1, 4], [2, 3], [5]].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

A sorted array of integers.

Guaranteed constraints:
0 ≤ arr.length ≤ 50,
1 ≤ arr[i] ≤ num.

[input] integer num

A non-negative integer.

Guaranteed constraints:
0 ≤ num ≤ 1000.

[output] array.array.integer

A sorted array containing sorted subsets composed of elements from arr 
that have a sum of num. It is guaranteed that there are no more than 1000 
subsets in the answer.
"""

def sumSubsets(lst, sumNum):
    if not lst or sumNum == 0: return [[]]
    results, dic = [], {}
    for i in range(len(lst)):
        if lst[i] == sumNum:
            if str(lst[i]) not in dic:
                dic[str(lst[i])] = 0
                results.append([lst[i]])
        elif lst[i] > sumNum or (i + 1 == len(lst)):
            return results
        else:
            subResults = sumSubsets(lst[i+1:len(lst)], sumNum - lst[i])
            for s in subResults:
                if str([lst[i]] + s) not in dic:
                    dic[str([lst[i]] + s)] = 0
                    results.append([lst[i]] + s)
    return results

print(sumSubsets([1, 2, 3, 4, 5], 5)) # [[1, 4], [2, 3], [5]]
print(sumSubsets([1, 2, 4], 0)) # [[]]

