
""" orderTask
You are given a set of tasks which are uniquely identified by integer IDs 
and a set of dependencies that define which tasks must be executed prior 
to others.

Your task is to

    write a function that orders the tasks so that all dependencies are 
    satisfied
    print to the standard output (stdout) all ordered task IDs separated 
    by a white space (on a single line)

Note that your function will receive the following arguments:

    dependencyFirst
        which is an array of integers giving the ID of the task that needs 
        to be executed first in each dependency
    dependencySecond
        which is an array of integers giving the ID of the task that needs 
        to be executed second in each dependency
    totalNumTasks
        which is an integer value giving the total number of tasks in the set

The ith dependency is described as follows: the ith task in dependencyFirst 
must be executed prior to the ith task in dependencySecond.

Data constraints

    the number of tasks in each collection will not be higher than 10,000
    within a collection of N tasks all the IDs are integers in the [1,N] range
    for a given set of tasks there may be multiple ways of ordering it to 
    satisfy the dependencies and any of them is accepted as a correct solution

Efficiency constraints

    your function is expected to print the result in less than 2 seconds

Example
Input 	                               Output

dependencyFirst: 3, 1, 2               3 1 5 2 4 6
dependencySecond: 2, 2, 4
num_total_tasks: 6

Explanation

    The set contains 6 tasks and they will be identified by IDs=1,2,3,4,5,6
    Task 3 must be executed prior to task 2, task 1 must be executed prior 
    to task 2 and task 2 must be executed prior to task 4
    One order that satisfies the three dependencies is: 3, 1, 5, 2, 4, 6
"""

# untested in vetted test cases, not 100% sure if it is right or efficient, 
# but performed well on test module for big numbers
def orderTask(df, ds, n):
    result, dic, setRes, setDs = [], {}, set(), set(ds)
    tasks = [i for i in range(1, n+1)]
    for i in range(len(df)):
        if df[i] not in setDs: 
            if df[i] not in setRes: 
                result.append(df[i])
                setRes.add(df[i])
        elif df[i] not in dic: dic[df[i]] = [ds[i]]
        else: dic[df[i]].append(ds[i])
    for key, value in dic.items():
        if key not in setRes: 
            result.append(key)
            setRes.add(key)
        for v in value:
            if v in setRes:
                result.remove(v)
                result.append(v)
    for value in dic.values():
        for v in value:
            if v in setRes: 
                result.remove(v)
                result.append(v)
    for i in range(len(tasks)):
        if tasks[i] not in setRes: result.append(tasks[i])
    for i in result:
        print(i, end=' ')
    print()


#test values
orderTask([3, 1, 2], [2, 2, 4], 6) 
# 3 1 5 2 4 6 (other answers possible, ex: 3 1 2 4 5 6)
orderTask([3, 1, 2, 1], [2, 2, 4, 3], 7) 
# 1 3 2 4 5 6 7 (??? not fully vetted, there may be other correct answers)

""" test module for big numbers
import time
import random
def testF():
    count = 1
    random.seed()
    for i in range(count):
        test = random.sample(range(5000), 5000)
        test2 = random.sample(range(5000), 5000)
        start = time.time()
        orderTask(test, test2, 10000)
        end = time.time()
        print('last result time in seconds:', end - start)
testF()
"""

