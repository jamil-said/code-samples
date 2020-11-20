""" countPrimes
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 1 if n > 2 else 0
        not_primes = [0] * n
        for i in range(3, n, 2):
            if not not_primes[i]:
                count += 1
                for j in range(i, n, 2):
                    if j * i >= n:
                        break
                    not_primes[i*j] = 1
        return count


print(Solution().countPrimes(10)) #4
print(Solution().countPrimes(2)) #0
print(Solution().countPrimes(1)) #0
print(Solution().countPrimes(0)) #0
print(Solution().countPrimes(100)) #25
print(Solution().countPrimes(1000)) #168
print(Solution().countPrimes(499979)) #41537
