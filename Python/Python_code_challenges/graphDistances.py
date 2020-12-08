
""" graphDistances -- 45 min
You have a connected directed graph that has positive weights in the 
adjacency matrix g. The graph is represented as a square matrix, where 
g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

Given g and the index of a start vertex s, find the minimal distances 
between the start vertex s and each of the vertices of the graph.

Example

For

g = [[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]]
and s = 0, the output should be
graphDistances(g, s) = [0, 2, 2].

Example

The distance from the start vertex 0 to itself is 0.
The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
The distance from the start vertex 0 to vertex 2 is 2.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer g

The graph is represented as a square matrix, as described above.

Guaranteed constraints:
1 ≤ g.length ≤ 100,
g.length = g[i].length,
-1 ≤ g[i][j] ≤ 30.

[input] integer s

The start vertex (0-based).

Guaranteed constraints:
0 ≤ s < g.length.

[output] array.integer

An array, the ith element of which is equal to the distance between the 
start vertex s and the ith vertex of the graph g.
"""

from heapq import heappush, heappop
def graphDistances(matrix, startVtx):
    results, h = {}, [(0, startVtx)]
    while h:
        dist, node = heappop(h)
        if node in results: continue
        results[node] = dist
        for idx, elem in enumerate(matrix[node]):
            if elem != -1 and idx not in results:
                heappush(h, (dist + elem, idx))
    return list(results.values())

print(graphDistances([[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]], 0))

