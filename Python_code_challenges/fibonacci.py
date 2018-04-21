"""
Create a function that calculates the first n fibonacci numbers in an 
efficient way (no recursion!)
"""

def myfib(n):
    a, b, c = 0, 1, 1
    results = []
    while c <= n:  
        results.append(b)
        a, b, c = b, a+b, c + 1
    return results

print(myfib(100))
