
""" asciiDeleteDistance
The deletion distance between two strings is the minimum sum of ASCII values
of characters that you need to delete in the two strings in order to have
the same string. the deletion distance between "cat" and "at" is 99, because 
you can just delete the first character of cat and the ASCII value of 'c' 
is 99. The deletion distance between "cat" and "bat" is 98 + 99, because 
you need to delete the first character of both words. Of course, the deletion
distance between two strings can't be greater than the sum of their total
ASCII values, because you can always delete both of the strings entirely. 
Implement an efficient function to find the deletion distance between two 
strings. 
"""

def delDis(s1, s2):
    if len(s1) < len(s2): s1, s2 = s2, s1
    dp = [0] * (len(s2)+1)
    for i in range(1, len(s1)+1):
        tmp = [0]
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]: tmp.append(dp[j-1] + ord(s1[i-1]))
            else: tmp.append(max(tmp[-1], dp[j]))
        dp = tmp[:]
    return sum(map(ord, s1+s2)) - 2 * dp[-1]


""" alternative, slower
def delDis(str1, str2):
    lenStr1, lenStr2 = len(str1), len(str2)
    matchC = [[0] * (lenStr2+1) for x in range(lenStr1+1)]
    for i in range(lenStr1):
        for j in range(lenStr2):
            if str1[i] == str2[j]:
                matchC[i+1][j+1] = matchC[i][j] + ord(str1[i])
            else:
                matchC[i+1][j+1] = max(matchC[i][j+1], matchC[i+1][j])
    dltDis = sum(map(ord, str1+str2)) - matchC[lenStr1][lenStr2] * 2
    return dltDis
"""

print(delDis('', 'cat')) #312
print(delDis('cat', '')) #312
print(delDis('cat', 'cat')) #0
print(delDis('at', 'cat')) #99
print(delDis('boat', 'got')) #298
print(delDis('thought', 'sloughs')) #674
print(delDis('cat', 'bat')) #197
print(delDis('sea', 'eat')) #231
print(delDis('row', 'cat')) #656


