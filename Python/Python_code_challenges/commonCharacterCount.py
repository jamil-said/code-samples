""" commonCharacterCount
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string s1

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ s1.length < 15.

    [input] string s2

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ s2.length < 15.

    [output] integer
"""


def commonCharacterCount(s1, s2):
    s1_dic, s2_dic = {}, {}
    res = 0
    for i in s1:
        if i in s1_dic:
            s1_dic[i] += 1
        else:
            s1_dic[i] = 1
    for i in s2:
        if i in s2_dic:
            s2_dic[i] += 1
        else:
            s2_dic[i] = 1
    for key, ele in s1_dic.items():
        if key in s2_dic:
            res += min(s1_dic[key], s2_dic[key])
    return res


print(commonCharacterCount("aabcc", "adcaa")) #3
print(commonCharacterCount("abca", "xyzbac")) #3
