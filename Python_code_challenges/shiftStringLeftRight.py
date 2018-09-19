
""" shiftStringLeftRight
Given a non-empty string 's' containing English alphabet letters, and two 
positive integers 'leftS' and 'rightS', create the most efficient possible 
function that returns the string 's' modified in the following manner: 
for each unit in the integer 'leftS', shift the string 's' one character 
to the left (i.e.: the first character becomes the last character) and 
for each unit in the integer 'rightS', shift the string 's' one character 
to the right (i.e.: the last character becomes the first character).

For example:

shiftLR('abcde', 1, 2) should return 'eabcd'

Explanation: the first integer argument 'leftS' is equal to 1, thus 
transforming the string into 'bcdea'. After that, the second integer 
argument 'rightS' is equal to 2, thus transforming the string into 'eabcd'.
"""

def shiftLR(s, leftS, rightS):
    if (leftS-rightS) % len(s) == 0: return s
    elif leftS > rightS: 
        leftS -= rightS
        if leftS > len(s): leftS = leftS % len(s)
        return s[leftS:] + s[:leftS]
    else: 
        rightS -= leftS
        if rightS > len(s): rightS = rightS % len(s)
        return  s[-rightS:] + s[:len(s)-rightS]

print(shiftLR('abcde', 1, 2)) # eabcd
print(shiftLR('abcde', 8, 8)) # abcde
print(shiftLR('abcde', 29, 8)) # bcdea
print(shiftLR('abcde', 8, 29)) # eabcd
print(shiftLR('abcde', 4032, 4004)) # deabc
print(shiftLR('abcdgsggdttrggfhfkldbdtgegfdwoiytjnmzapqoudbcbvcjkspetrgryryjjdjdjdjdrn', 4032, 4002)) # iytjnmzapqoudbcbvcjkspetrgryryjjdjdjdjdrnabcdgsggdttrggfhfkldbdtgegfdwo
print(shiftLR('abcdgsggdttrggfhfjsyegrpoanncvzmaldptehawqiefghatryropdfhyryryjjdjdjdjtr', 4032, 42)) # zmaldptehawqiefghatryropdfhyryryjjdjdjdjtrabcdgsggdttrggfhfjsyegrpoanncv

