""" palindromeRearranging
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 50.

    [output] boolean

    true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""


def palindromeRearranging(s):
    dic = {}
    count = 0
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for v in dic.values():
        if v % 2 != 0:
            count += 1
    return True if (count == 1 and len(s) % 2 != 0) or (count == 0 and len(s) % 2 == 0) else False


print(palindromeRearranging("abbcabb")) # True
print(palindromeRearranging("zyyzzzzz")) # True
