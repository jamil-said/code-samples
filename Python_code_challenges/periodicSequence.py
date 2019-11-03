
""" 20min -- periodicSequence
A periodic sequence s is defined as follows:

s[0], a, b and m are all given positive integers;
s[i] for i > 0 is equal to (a * s[i - 1] + b) mod m.
Find the period of s, i.e. the smallest integer T such that for each 
i > k (for some integer k): s[i] = s[i + T].

Example

For s0 = 11, a = 2, b = 6 and m = 12, the output should be
periodicSequence(s0, a, b, m) = 2.

The sequence would look like this: 11, 4, 2, 10, 2, 10, 2, 10, 2, 10....

For s0 = 1, a = 2, b = 3 and m = 5, the output should be
periodicSequence(s0, a, b, m) = 4.

The sequence would look like this: 1, 0, 3, 4, 1, 0, 3, 4, 1, 0, 3, 4....

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer s0

a positive integer representing s[0].

Guaranteed constraints:
1 ≤ s0 ≤ 100,
s0 < m.

[input] integer a

Guaranteed constraints:
2 ≤ a ≤ 100.

[input] integer b

Guaranteed constraints:
2 ≤ b ≤ 100.

[input] integer m

Guaranteed constraints:
5 ≤ m ≤ 100.

[output] integer

The sequence period.
"""

def periodicSequence(s0, a, b, m):
    seq, dicSeq, x = [], {}, 1
    seq.append(s0)
    dicSeq[s0] = 0
    while True:
        seqElem = (a * seq[x-1] + b) % m
        seq.append(seqElem)
        if seqElem not in dicSeq:
            dicSeq[seqElem] = x
        else:
            return x - dicSeq[seqElem]
        x += 1

print(periodicSequence(11, 2, 6, 12)) #2
print(periodicSequence(1, 2, 3, 5)) #4

