""" firstNotRepeatingCharacter -- 15min
Note: Write a solution that only iterates over the string once and uses 
O(1) additional memory, since this is what you would be asked to do during 
a real interview.

Given a string s, find and return the first instance of a non-repeating 
character in it. If there is no such character, return '_'.

Example

    For s = "abacabad", the output should be
    firstNotRepeatingCharacter(s) = 'c'.

    There are 2 non-repeating characters in the string: 'c' and 'd'. 
    Return c since it appears in the string first.

    For s = "abacabaabacaba", the output should be
    firstNotRepeatingCharacter(s) = '_'.

    There are no characters in this string that do not repeat.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string s

    A string that contains only lowercase English letters.

    Guaranteed constraints:
    1 ≤ s.length ≤ 105.

    [output] char

    The first non-repeating character in s, or '_' if there are no 
    characters that do not repeat.

"""

def firstNotRepeatingCharacter(s):
    chars, count = [], {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1 
            chars.append(c)
    for c in chars:
        if count[c] == 1:
            return c
    return '_'

print(firstNotRepeatingCharacter("abacabad"))
print(firstNotRepeatingCharacter("abacabaabacaba"))


