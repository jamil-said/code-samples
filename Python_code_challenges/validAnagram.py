
""" validAnagram 
Given two strings s and t, write a function to determine if t is an 
anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your 
solution to such case?
### answer to follow up: anagrams would be checked for diferent  characters 
### as well. But if want only english could filter by unicode numbers or
### membership check on a dictionary (set) with the valid characters
"""

#best performance solution (86% percentile)
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dic = {}
        for c in s:
            if c in dic: dic[c] += 1
            else: dic[c] = 1
        for c in t:
            if c in dic: 
                dic[c] -= 1
                if dic[c] < 0: return False
            elif c not in dic: return False
        return True

""" alternative, slower (53% percentile)
class Solution:
    def isAnagram(self, s, t):
        return sorted(list(s)) == sorted(list(t))
"""

""" alternative, even slower than version with list (29% percentile)
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
"""

print(Solution().isAnagram("anagram", "nagaram")) #True
print(Solution().isAnagram("ab", "a")) #False

