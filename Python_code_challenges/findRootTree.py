""" findRootTree
You have a tree represented as parent/child tuples like this:

[(28, 26), (82, 69), (28, 41), (82, 91), (37, 22), (37, 28), (41, 45), (46, 37), (91, 85), (46, 60), (60, 82), (60, 50)]

Write a function that returns the root of the tree. Return the root value as integer (in the example above, the answer is 46).
"""

def find_root(a):
    set_a, set_b = set(), set()
    for ele in a:
        set_a.add(ele[0])
        set_b.add(ele[1])
    return list(set_a-set_b)[0]

print(find_root([(28, 26), (82, 69), (28, 41), (82, 91), (37, 22), (37, 28), (41, 45), (46, 37), (91, 85), (46, 60), (60, 82), (60, 50)])) #46
