
""" towerHanoi
Tower of Hanoi is a mathematical puzzle where we have three rods and n 
disks. The objective of the puzzle is to move the entire stack to another 
rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and 
placing it on top of another stack i.e. a disk can only be moved if it is 
the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.

Input: n= number of disks

Extra: return the number of moves required to complete the tower
"""

def towerHanoi(n, fromRod, toRod, auxRod):
    calcHanoi(n, fromRod, toRod, auxRod)
    return (2**n)-1
    
def calcHanoi(n, fromRod, toRod, auxRod):
    if n == 1:
        print("Moving disk 1 from rod", fromRod, "to rod", toRod)
        return
    towerHanoi(n-1, fromRod, auxRod, toRod)
    print("Moving disk", n, "from rod", fromRod, "to rod", toRod)
    towerHanoi(n-1, auxRod, toRod, fromRod)

print(towerHanoi(4, 'A', 'C', 'B')) #15



