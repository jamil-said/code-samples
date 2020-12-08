
""" braces
Given an array of strings containing three types of braces: round (), 
square [] and curly {}

Your task is to

write a function that checks whether the braces in each string are 
correctly matched
prints 1 to standard output (stdout) if the braces in each string are 
matched and 0 if they're not (one result per line)

Note that your function will receive the following arguments:

expressions
    which is an array of strings containing braces

Data constraints

the length of the array will not exceed 100
the length of any string will not exceed 5000

Efficiency constraints

your function is expected to print the result in less than 2 seconds

Example Input Output

expressions: [ ")(){}", "", "([])", "{()[]}", "([)]" ]

0 1 1 1 0
"""

def isMatched(arr):
    for st in arr: print(calcMatched(st))

def calcMatched(s):
    stack, setOp, dicCl = [], {'(','{','['}, {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in setOp: 
            stack.append(c)
        elif c in dicCl: 
            if len(stack) == 0 or stack.pop() != dicCl[c]: return 0
    return 1 if len(stack) == 0 else 0


isMatched([")(){}", "[]({})", "([])", "{()[]}", "([)]"])
"""
0
1
1
1
0
"""
