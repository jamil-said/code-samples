
""" swapLexOrder  -- 45 min.
Given a string str and array of pairs that indicates which indices in 
the string can be swapped, return the lexicographically largest string 
that results from doing the allowed swaps. You can swap indices any number 
of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", 
"dbca". The lexicographically largest string in this list is "dbca".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string str

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ str.length ≤ 104.

[input] array.array.integer pairs

An array containing pairs of indices that can be swapped in str (1-based). 
This means that for each pairs[i], you can swap elements in str that have 
the indices pairs[i][0] and pairs[i][1].

Guaranteed constraints:
0 ≤ pairs.length ≤ 5000,
pairs[i].length = 2.

[output] string
"""

def swapLexOrder(strg, pairs):
    dic, lenStr = {}, len(strg)
    result = ['0' for i in range(lenStr)]
    visited = [False for i in range(lenStr)]
    for i in range(len(pairs)):
        if pairs[i][0] - 1 in dic:
            dic[pairs[i][0] - 1].append(pairs[i][1] - 1)
        else:
            dic[pairs[i][0] - 1] = [pairs[i][1] - 1]
        if pairs[i][1] - 1 in dic:
            dic[pairs[i][1] - 1].append(pairs[i][0] - 1)
        else:
            dic[pairs[i][1] - 1] = [pairs[i][0] - 1]
    for charIndex in range(lenStr):
        curr = []
        if not visited[charIndex]:
            visited[charIndex] = True
            curr.append(charIndex)
            resulCalc = calcSwap(dic, visited, charIndex, curr)
            resulCalc = sorted(resulCalc)
            r = [strg[i] for i in resulCalc]
            r = sorted(r, reverse=True)
            for ind, i in enumerate(r):
                result[resulCalc[ind]] = r[ind]
    return ''.join(result)

def calcSwap(dic, visited, charIdx, curr):
    if charIdx in dic:
        for idx in dic[charIdx]:
            if not visited[idx]:
                visited[idx] = True
                curr.append(idx)
                calcSwap(dic, visited, idx, curr)
    return curr


print(swapLexOrder("abdc", [[1, 4], [3, 4]])) # "dbca"
print(swapLexOrder("acxrabdz", [[1,3], [6,8], [3,8], [2,7]])) # "zdxrabca"

