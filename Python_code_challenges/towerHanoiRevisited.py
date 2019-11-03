
""" towerHanoiRevisited
Given 3 three pegs: leftmost peg A, middle peg B and rightmost peg C.Find 
the shortest sequence of moves that transfers a tower of n disks from the 
left peg A to the right peg C, if direct moves between A and C are disallowed. 
(Each move must be to or from the middle peg B.)

Constraints:
1. Initially the left peg A in stacked by n disks in the order of decreasing 
size.
2. Only one move cand be done at a time and never moving a larger one onto 
a smaller.
3. Number of moves will always be less than 2^64.
4. 1 <= n <= 35

Input
Input begins with a integer t, followed by t lines. Each line has the no. 
of disks n.

Output
For each test case, output the minimum no. of move required to transfer 
the n disks from peg A to peg C.
"""

def hanoi(t, arr):
    for i in range(t): print((3**arr[i])-1)

hanoi(4, [1, 2, 5, 10])
"""
2
8
242
59048
"""

