
""" letterCombinationsPhoneNumber
Given a digit string, return all possible letter combinations that the 
number could represent.

A mapping of digit to letters (just like on the telephone buttons) is 
given below.

2:abc, 3:def, 4:ghi, 5:jkl, 6:mno, 7:pqrs, 8:tuv, 9:wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could 
be in any order you want.
"""

class Solution:
    def letterCombinations(self, dig):
        """
        :type dig: str
        :rtype: List[str]
        """
        if not dig: return []
        result, dp = [], ['']
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],\
        '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], \
        '8':['t','u','v'], '9':['w','x','y','z']}
        for i in range(len(dig)):
            temp = [] #move this into next loop if want to consider input '1', etc
            if dig[i] in dic:
                for j in dic[dig[i]]:
                    for k in dp: temp.append(k+j)
            dp = temp[:]
        return dp #sorted(dp)            

#note: answers below may have alternates because answer sorting is not required
print(Solution().letterCombinations("23"))
# ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(Solution().letterCombinations("2")) #['a', 'b', 'c']


