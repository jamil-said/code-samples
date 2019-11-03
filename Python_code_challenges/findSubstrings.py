
""" findSubstrings -- 40 min
You have two arrays of strings, words and parts. Return an array that 
contains the strings from words, modified so that any occurrences of the 
substrings from parts are surrounded by square brackets [], following these 
guidelines:

If several parts substrings occur in one string in words, choose the longest 
one. If there is still more than one such part, then choose the one that 
appears first in the string.

Example

For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", 
"mel", "lon", "el", "An"], the output should be
findSubstrings(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", 
"Water[mel]on"].

While "Watermelon" contains three substrings from the parts array, "a", 
"mel", and "lon", "mel" is the longest substring that appears first in 
the string.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string words

An array of strings consisting only of uppercase and lowercase English 
letters.

Guaranteed constraints:
0 ≤ words.length ≤ 104,
1 ≤ words[i].length ≤ 30.

[input] array.string parts

An array of strings consisting only of uppercase and lower English 
letters. Each string is no more than 5 characters in length.

Guaranteed constraints:
0 ≤ parts.length ≤ 105,
1 ≤ parts[i].length ≤ 5,
parts[i] ≠ parts[j].

[output] array.string
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}

def findSubstrings(words, parts):
    if not words: return []
    if not parts: return words
    root = TrieNode('')
    for p in parts:
        addPartToTrie(root, p)
    return [searchWord(w, root) for w in words]

def addPartToTrie(root, part):
    currentNode = root
    for char in part:
        if char not in currentNode.children:
            currentNode.children[char] = TrieNode(char)
        currentNode = currentNode.children[char]
    currentNode.end = True

def searchWord(w, root):
    lenLrgSbstr, lgstIdx = 0, 0
    for idxStart in range(len(w)):
        currNode = root
        for idxChar in range(idxStart, len(w)):
            char = w[idxChar]
            if char not in currNode.children:
                break
            currNode = currNode.children[char]
            lenTemp = idxChar - idxStart + 1
            if currNode.end and lenTemp > lenLrgSbstr:
                lenLrgSbstr = lenTemp
                lgstIdx = idxStart
    if lenLrgSbstr == 0: return w
    endIdx = lgstIdx + lenLrgSbstr
    return w[:lgstIdx] + "[" + w[lgstIdx: endIdx] + "]" + w[endIdx:]


print(findSubstrings(["Apple", "Melon", "Orange", "Watermelon"], 
["a", "mel", "lon", "el", "An"])) 
# ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"]
print(findSubstrings(["coccidiosis"], ["d", "i"])) # ["cocc[i]diosis"]  
print(findSubstrings(["aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"], [
 "aaaaa", 
 "bbbbb", 
 "a", 
 "aa", 
 "aaaa", 
 "aaa", 
 "aaaab"])) # ["[aaaaa]aaaaaaaaaaaaaaaaaaaaaaaab"]

