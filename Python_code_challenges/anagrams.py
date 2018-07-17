
""" Anagrams 
Two words are considered anagrams if by rearranging the letters of the 
first word we get the second word. For instance cinema and iceman are anagrams.

Given a list of word pairs

Your task is to

write a function that determines for each pair if it’s an anagram or not
for each pair of words your function will print to standard output (stdout) 
the value 1 if the pair is an anagram or 0 otherwise (one result per line)

Note that your function will receive the following arguments:

firstWords
    which is an array of strings giving the first word for each of the pairs
secondWords
    which is an array of strings giving the corresponding second word

Data constraints

the number of word pairs will not exceed 100
the maximum length of any word in the pairs will not exceed 100 characters
all words will contain only lowercase English letters (a-z)

Efficiency constraints

your function is expected to print the result in less than 2 seconds

Example Input Output

firstWords: “cinema”, “host”, “aba”, “train” 
secondWords: “iceman”, “shot”, “bab”, “rain”

1 1 0 0
"""

def checkAnagram(fw, sw):
    for i in range(len(fw)):
        if sorted(list(fw[i])) == sorted(list(sw[i])): print(1)
        else: print(0)

""" alternative, slower
def checkAnagram(fw, sw):
    for i in range(len(fw)):
        if sorted(fw[i]) == sorted(sw[i]): print(1)
        else: print(0)
"""

checkAnagram(["cinema", "host", "aba", "train"], [
"iceman", "shot", "bab", "rain"])
"""
1
1
0
0
"""

