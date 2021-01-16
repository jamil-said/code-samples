""" nearestPostalDelivery
You are in charge of calculating the shortest path to deliver mail to a 
certain number of locations. Consider that your delivery map is like a 
flat cartesian plane, and that the delivery truck starts at point [0, 0]. 
You are given an integer number "n" of locations to deliver mail to and 
an array "arr" of integer coodinates [x, y] that represent several delivery 
locations to choose from. 

Create a function that returns a 2-dimensional array with the coordinates 
representing the shortest path to deliver mail to a "n" number of locations. 
The distance between point [x0, y0] to point [x1, y1] is the length of the straight 
line between the two points. If some paths have the same lenght, you may use any of 
the tying paths you want (or both) to fulfill the 'n' number of deliveries. The array 
"arr" is guaranteed to have at least two delivery locations and the number "n" is 
guaranteed to be a non-zero positive integer that is equal or smaller than the 
number of delivery locations.

Example:

for values:
n = 2
arr = [[1, 3], [4, 7], [1, -1]]

the expected output would be:
[[1, -1], [1, 3]]
"""

# I think this solution is right, but it was not tested with a large test case
def nearDeliver(n, arr):
    res = [float('inf')]
    for i in range(len(arr)):
        calc([], arr[:i]+arr[i+1:]+[arr[i]], [], res, n)
    return res[-2]
    
def calc(path, arr, dist, res, n):
    if res[-1] <= sum(dist):
        return
    if len(dist) == n:
        return res.extend([path, sum(dist)])
    pop_arr = arr.pop()
    if not path:
        dist.append((((pop_arr[0]**2)+(pop_arr[1]**2))**0.5))
    else:
        dist.append((((((pop_arr[0]-path[-1][0])**2)+((pop_arr[1]-path[-1][1])**2))**0.5)))
    path.append(pop_arr)
    for i in range(len(arr)):
        calc(path[:], arr[:i]+arr[i+1:]+[arr[i]], dist[:], res, n)


print(nearDeliver(2, [[1, 3], [4, 7], [1, -1]])) # [[1, -1], [1, 3]]
print(nearDeliver(2, [[1, 3], [4, 7], [1, -1], [1, 2], [3, 4]])) # [[1, 2], [1, 3]]
print(nearDeliver(2, [[1, 5], [4, 7], [1, -1], [1, 2], [3, 4]])) # [[1, -1], [1, 2]]
print(nearDeliver(3, [[1, 3], [4, 7], [1, -1], [1, 2], [3, 4], [5, 8]])) # [[1, -1], [1, 2], [1, 3]]
