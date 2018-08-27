
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
strings. You can refer to the Wikipedia article on the algorithm for edit 
distance if you want to. The algorithm there is not quite the same as the 
algorithm required here, but it's similar.
"""

def delDis(s1, s2):
    dp = [0] * (len(s2)+1)
    for i in range(1, len(s1)+1):
        tmp = [0]
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]: tmp.append(dp[j-1] + ord(s1[i-1]))
            else: tmp.append(max(tmp[-1], dp[j]))
        dp = tmp[:]
    return sum(map(ord, s1+s2)) - 2 * dp[-1]


""" alternative, slower, but smaller and more intuitive
def delDis(s1, s2):
    dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]: dp[i+1][j+1] = dp[i][j]+ord(s1[i])
            else: dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return sum(map(ord, s1+s2)) - 2 * dp[-1][-1]
"""

print(delDis('', 'cat')) #312
print(delDis('cat', '')) #312
print(delDis('cat', 'cat')) #0
print(delDis('at', 'cat')) #99
print(delDis('boat', 'got')) #298
print(delDis('got', 'boat')) #298
print(delDis('thought', 'sloughs')) #674
print(delDis('cat', 'bat')) #197
print(delDis('sea', 'eat')) #231
print(delDis('row', 'cat')) #656


