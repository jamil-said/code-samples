
""" minSubstringWithAllChars -- 30 min.
You have two strings, s and t. The string t contains only unique elements. 
Find and return the minimum consecutive substring of s that contains all o
f the elements from t.

It's guaranteed that the answer exists. If there are several answers, 
return the one which starts from the smallest index.

Example

For s = "adobecodebanc" and t = "abc", the output should be
minSubstringWithAllChars(s, t) = "banc".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string consisting only of lowercase English letters.

Guaranteed constraints:
0 ≤ s.length ≤ 100.

[input] string t

A string consisting only of unique lowercase English letters.

Guaranteed constraints:
0 ≤ t.length ≤ min(26, s.length).

[output] string
"""

def minSubstringWithAllChars(s1, s2):
    if not s1 or not s2: return ''
    dic, idxFirst = {}, 0
    idxLast, s2Lst = len(s1), list(s2)
    for char in s2:
        dic[char] = []
    for i in range(idxLast):
        if s1[i] in s2:
            if s1[i] not in s2Lst and dic[s1[i]] != []:
                dic[s1[i]].pop(0)
            elif s1[i] in s2Lst:
                s2Lst.remove(s1[i])
            dic[s1[i]].append(i)
        if s2Lst == []:
            tempLst = [x[0] for x in dic.values()]
            maximum, minimum = max(tempLst), min(tempLst)
            if maximum-minimum+1 < idxLast-idxFirst+1:
                idxFirst, idxLast = minimum, maximum
    return '' if s2Lst != [] else s1[idxFirst:idxLast+1]


print(minSubstringWithAllChars("adobecodebanc", "abc")) # "banc"
print(minSubstringWithAllChars("tvdsxcqsnoeccaurocnk", "acqt")) # "tvdsxcqsnoecca"
