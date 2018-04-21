
""" knapsackRobber
Suppose you are a computer scientist/art thief who has broken into a major 
art gallery. All you have with you to haul out your stolen art is your 
knapsack, which only holds W pounds of art. For every piece of art you 
know its value (val interger array) and its weight (wt interger array). 
Write a dynamic programming function to help you maximize your profit.
"""

def knapSack(maxW, wgt, val):
    knapS = [[0 for i in range(maxW+1)] for j in range(len(val)+1)]
    for v in range(len(val)+1):
        for w in range(maxW+1):
            if v==0 or w==0:
                knapS[v][w] = 0
            elif wgt[v-1] <= w:
                knapS[v][w] = max(val[v-1] + knapS[v-1][w-wgt[v-1]], knapS[v-1][w])
            else:
                knapS[v][w] = knapS[v-1][w]
    return knapS[len(val)][maxW]

print(knapSack(50, [10, 20, 30], [60, 100, 120])) #220

