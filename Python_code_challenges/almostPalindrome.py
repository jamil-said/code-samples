
"""
The Palindromic score of a string is the number of errors (characters which
do not match) when the string is read forwards and backwards. For example, 
the palindromic score of 'fox' is 2, because 'fox' and 'xof' differ by two
characters. Write a function to take a string and return its palindromic 
score. 
"""

def apalin(word):
    palindex = 0
    for i in range(len(word)): 
        if word[i] != word[len(word)-i-1]: palindex += 1
    return palindex

print(apalin('abba')) #0
print(apalin('abcdcaa')) #2
print(apalin('fox')) #2
print(apalin('aaabbb')) #6
