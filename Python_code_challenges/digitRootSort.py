
""" 15min -- digiRootSort
Digit root of some positive integer is defined as the sum of all of its 
digits.

You are given an array of integers. Sort it in such a way that if a comes 
before b then the digit root of a is less than or equal to the digit root 
of b. If two numbers have the same digit root, the smaller one (in the 
regular sense) should come first. For example 4 and 13 have the same digit 
root, however 4 < 13 thus 4 comes before 13 in any digitRoot sorting where 
both are present.

Example

For a = [13, 20, 7, 4], the output should be [20, 4, 13, 7].

[execution time limit] 4 seconds (py3)

[input] array.integer a

Array of positive integers.

[output] array.integer
"""

#this version is optimized from alternative answer, but not tested with full test case
def digitRootSort(a):
    dr, drDic, tempLst, result  = 0, {}, [], []
    for i, elem in enumerate(a):
        dr = sum(map(int, str(elem)))
        if dr in drDic: drDic[dr].append(i)
        else: drDic[dr] = [i]
        dr = 0
    for key, value in drDic.items():
        if len(value) == 1:
            result.append(a[value[0]])
        else:
            for n in value:
                tempLst.append(a[n])
            result.extend(sorted(tempLst))
            tempLst = []
    return result


print(digitRootSort([13, 20, 7, 4])) #[20, 4, 13, 7]

""" alternative, passed full test case
def digitRootSort(a):
    dr, drDic, tempLst, result  = 0, {}, [], []
    for i, elem in enumerate(a):
        dr = sum(map(int, str(elem)))
        if dr in drDic: drDic[dr].append(i)
        else: drDic[dr] = [i]
        dr = 0
    for k in range(max(drDic.keys())+1):
        if k in drDic:
            if len(drDic[k]) == 1:
                result.append(a[drDic[k][0]])
            else:
                for n in drDic[k]:
                    tempLst.append(a[n])
                result.extend(sorted(tempLst))
                tempLst = []
    return result
"""


