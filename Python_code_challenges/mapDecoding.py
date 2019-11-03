
""" mapDecoding  -- 30 min.
A top secret message containing uppercase letters from 'A' to 'Z' has 
been encoded as numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent and you need to determine the total number of ways 
that the message can be decoded.

Since the answer could be very large, take it modulo 109 + 7.

Example

For message = "123", the output should be

mapDecoding(message) = 3.

"123" can be decoded as "ABC" (1 2 3), "LC" (12 3) or "AW" (1 23), so 
the total number of ways is 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string message

A string containing only digits.

Guaranteed constraints:

0 ≤ message.length ≤ 105.

[output] integer

The total number of ways to decode the given message.
"""

def mapDecoding(message):
    if not message: return 1
    msgLen = len(message)
    dp = [0] * (msgLen + 1)
    dp[0] = 1
    for i in range(1, msgLen + 1):
        if message[i-1] != '0':
            dp[i] += dp[i-1]
        if len(message[i-2:i]) == 2 and '10' <= message[i-2:i] <= '26':
            dp[i] += dp[i-2]
    return dp[msgLen] % 1000000007

print(mapDecoding('123')) # 3
print(mapDecoding('10122110')) #5

