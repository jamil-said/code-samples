
""" launchSequenceChecker -- 10 min
The master launch sequence consists of several independent sequences for 
different systems. Your goal is to verify that all the individual system 
sequences are in strictly increasing order. In other words, for any two 
elements i and j (i < j) of the master launch sequence that belong to the 
same system (having systemNames[i] = systemNames[j]), their values should 
be in strictly increasing order (i.e. stepNumbers[i] < stepNumbers[j]).

Example

For systemNames = ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", 
"dragon"] and stepNumbers = [1, 10, 11, 2, 12, 111], the output should be
launchSequenceChecker(systemNames, stepNumbers) = true.

There are three independent sequences for systems "stage_1", "stage_2", 
and "dragon". These sequences are [1, 2], [10, 12], and [11, 111], 
respectively. The elements are in strictly increasing order for all three.

For systemNames = ["stage_1", "stage_1", "stage_2", "dragon"] and 
stepNumbers = [2, 1, 12, 111], the output should be
launchSequenceChecker(systemNames, stepNumbers) = false.

There are three independent sequences for systems "stage_1", "stage_2", 
and "dragon". These sequences are [2, 1], [12], and [111], respectively. 
In the first sequence, the elements are not ordered properly.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string systemNames

An array of non-empty strings. systemNames[i] contains the name of the 
system to which the ith element of the master launch sequence belongs.

Guaranteed constraints:
1 ≤ systemNames.length ≤ 5 · 104,
1 ≤ systemNames[i].length ≤ 10.

[input] array.integer stepNumbers

An array of positive integers. stepNumbers[i] contains the value of the 
ith element of the master launch sequence.

Guaranteed constraints:
stepNumbers.length = systemNames.length,
1 ≤ stepNumbers[i] ≤ 109.

[output] boolean

Return true if all the individual system sequences are in strictly 
increasing order, otherwise return false.
"""

def launchSequenceChecker(systemN, stepN):
    dic = {}
    for i, n in enumerate(systemN):
        if n not in dic: dic[n] = [stepN[i]]
        else: dic[n].append(stepN[i])
    for v in dic.values():
        if v != sorted(v) or len(set(v)) != len(v): return False
    return True

print(launchSequenceChecker(["stage_1", 
 "stage_1", 
 "stage_2", 
 "dragon"], [2, 1, 12, 111])) #False

