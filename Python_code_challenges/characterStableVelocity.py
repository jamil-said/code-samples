
""" characterStableVelocity
You are a video game developer. Your current task is to count all periods 
of time in which the character of the game had constant velocity (i.e.: 
zero acceleration). For that, you measured the character position in equally
distributed moments of time. The character is considered to be in constant 
speed if the difference between two consecutive position measurements remain 
the same (note that you need least three different measurements to ascertain that). 
Note also that some periods of time might be contained in others (see all examples).

For example:
2, 4, 6, 8 is stable (velocity 2)
5, 5, 5, 5 is stable (velocity 0)
5, 0, -5, -10 is stable (velocity -5)
0, 2 is not stable (need at least three measurements)
3, 3, 5, 8, 12 is not stable (changing velocity)

Write an EFFICIENT function/algorithm that given an array of intergers, 
returns the number of periods when the character's velocity was stable. 
The function should return -1 if the result exceeds 1,000,000,000.

More examples: 

Given input array arr = [-2, 0, 2, 2, 2, 1, 2, 1, 0,-1], the function should
return 5, because there are five periods in which the character's velocity 
was stable: (0,2), (2,4), (6,9), (6,8), and (7,9). Note that the last two
periods are contaiuned by (6,9).

For arr = [5, 5, 5,...] of length 10,000, the function should return 49985001
"""

def solution(arr):
    result, last = [0], [0]
    if len(arr) < 3: return 0
    def calcExtra(j, velo):
        if j < last[0]: 
            result[0] += last[0]-j
            return
        while j < len(arr)-1: 
            if arr[j]-arr[j+1] == velo: 
                result[0] += 1
                j += 1
                last[0] = j
            else: return
    for i in range(len(arr)-2):
        if arr[i]-arr[i+1] == arr[i+1]-arr[i+2]: 
            result[0] += 1
            calcExtra(i+2, arr[i]-arr[i+1])
    return result[0] if result[0] <= 1000000000 else -1


print(solution([-2, 0, 2, 2, 2, 1, 2, 1, 0,-1])) #5
print(solution([5]*10000)) #49985001

