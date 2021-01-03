""" shapeArea
Below we will define an n-interesting polygon. Your task is to find the 
area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An 
n-interesting polygon is obtained by taking the n - 1-interesting polygon 
and appending 1-interesting polygons to its rim, side by side. You can 
see the 1-, 2- and 3-interesting polygons in the picture below.

              X                    X
  X         X X X                X X X
              X                X X X X X
 n=1        n = 2                X X X
                                   X
                                 n = 3

Example

For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.
Input/Output

[execution time limit] 4 seconds (php)

[input] integer n

Guaranteed constraints:
1 ≤ n < 104.

[output] integer

The area of the n-interesting polygon.
"""


def shapeArea(n):
    # Centered square numbers
    return n**2 + (n-1)**2


print(shapeArea(2)) #5
print(shapeArea(3)) #13
print(shapeArea(7000)) #97986001

