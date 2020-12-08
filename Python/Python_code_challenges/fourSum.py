
""" fourSum
Given an array S of n integers, are there elements a, b, c, and d in S 
such that a + b + c + d = target? Find all unique quadruplets in the array 
which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, n, t):
        """
        :type n: List[int]
        :type t: int
        :rtype: List[List[int]]
        """
        result, end, n = [], len(n)-1, sorted(n)
        for i in range(end-2):
            if i > 0 and n[i] == n[i-1]: continue
            if sum(n[i:i+4]) > t: break
            if n[i] + sum(n[-3:]) < t: continue
            for j in range(i+1, end-1):
                if j > i+1 and n[j] == n[j-1]: continue
                if n[i] + sum(n[j:j+3]) > t: break
                if n[i] + n[j] + sum(n[-2:]) < t: continue
                k, l, part = j+1, end, t-n[i]-n[j]
                while k < l:
                    tmp = part - n[k] - n[l]
                    if tmp > 0:
                        k += 1
                    elif tmp < 0:
                        l -= 1
                    else:
                        result.append([n[i], n[j], n[k], n[l]])
                        while(k < l and n[k+1] == n[k]): k += 1
                        while(k < l and n[l-1] == n[l]): l -= 1
                        k, l = k+1, l-1
        return result

print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
"""
[[-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]]
  or variations of the above (result does not need to be sorted)
"""

""" alternative, slower
from collections import defaultdict
class Solution:
    def fourSum(self, n, t):
        n, result, dic, defDic = sorted(n), [], {}, defaultdict(list)
        for i in range(0, len(n)-1):
            for j in range(i+1, len(n)): 
                repeat = False
                for [x, y] in defDic[n[i]+n[j]]:
                    if n[x] == n[i]:
                        repeat = True
                        break
                if not repeat: defDic[n[i]+n[j]].append([i, j])
        for c in range(2, len(n)):
            for d in range(c+1, len(n)):
                if t-n[c]-n[d] in defDic:
                    for [a, b] in defDic[t-n[c]-n[d]]:
                        if b < c:
                            temp = [n[a], n[b], n[c], n[d]]
                            tempStr = ''.join(str(temp))
                            if tempStr not in dic:
                                dic[tempStr] = True
                                result.append(temp)
        return result #sorted(result)
"""


