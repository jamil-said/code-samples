
""" substringNSizeDistict
Given a string "s" and a positive integer "n", create a function that 
retrieves all "n" sized substrings of "s" that have no repeated characters 
on them. Return all the substrings in a list in the order they appear 
(from left to right) and without repeated substrings -- if there are repeated 
substrings, return only the first one to appear; if no substrings can be 
found, return an empty list.
"""

def findStrings(s, n):
    res, check = [], set()
    for i in range(len(s)-n+1):
        if len(s[i:i+n]) == len(set(s[i:i+n])): 
            if s[i:i+n] not in check:
                check.add(s[i:i+n])
                res.append(s[i:i+n])
    return res

print(findStrings("rwrglwnrgrwunrgwwwrgl", 4))  
# ['wrgl', 'rglw', 'glwn', 'lwnr', 'wnrg', 'grwu', 'rwun', 'wunr', 'unrg', 'nrgw']


