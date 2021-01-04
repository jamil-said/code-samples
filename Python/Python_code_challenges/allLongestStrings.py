""" allLongestStrings
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
"""


def allLongestStrings(inputArray):
    res = []
    temp = 0
    for i in inputArray:
        if len(i) > temp:
            res = []
            temp = len(i)
            res.append(i)
        elif len(i) == temp:
            res.append(i)
    return res


print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"])) #["aba", "vcd", "aba"]
print(allLongestStrings(["enyky", "benyky", "yely", "varennyky"])) #["varennyky"]
