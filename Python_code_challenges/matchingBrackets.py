
"""
A string of brackets is correctly matched if you can pair every opening 
bracket up with a later closing bracket. For example, "(()())" is correctly 
matched and "(()" and ")(" are not. Implement a function which takes a string 
of brackets and returns the minimum number of brackets you'd have to add 
to the string to make it correctly matched. For example, "(()" could be 
correctly matched by adding a single closing bracket at the end, so you 
would return 1. ")(" can be correctly matched by adding an opening bracket 
at the start and a closing bracket at the end, so you'd return 2. If your
string is already correctly matched, you can just return 0.
"""

def brackets(myString):
    tbc, wnbc, setOp, setCl = 0, 0, {'('}, {')'}
    for i in range(len(myString)):
        if myString[i] in setOp:
            tbc += 1
        elif myString[i] in setCl:
            if tbc > 0: tbc -= 1
            else: wnbc += 1
    return tbc + wnbc

""" Alternative, slower
def brackets(myString):
    tbc, wnbc = 0, 0  #to be closed, will not be closed
    for i in range(len(myString)):
        if myString[i] == '(':
            tbc += 1
        elif myString[i] == ')':
            if tbc > 0: tbc -= 1
            else: wnbc += 1
    return tbc + wnbc
"""  

print(brackets('(()()()())')) #0
print(brackets('(()())')) #0
print(brackets('((())')) #1
print(brackets('())')) #1
print(brackets(')(')) #2
print(brackets(')(())')) #1
print(brackets('))((()')) #4
print(brackets('))()')) #2
print(brackets(')((')) #3
print(brackets('(((')) #3
print(brackets(')))')) #3
print(brackets('ab())')) #1


