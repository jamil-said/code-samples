
""" gameBoardLights 
You are programming the behavior of a series of eight lights arranged in 
a straight line on the board of an electronic game. The lights can be either 
on or off. At every second that elapses, the lights will change (or not) 
their state according to the following pattern: if both neighbor lights 
are on or off, the light turns (or remains) off; otherwise, the light turns 
(or remains) on. For the edge lights that have only one neighbor, you may 
consider that the other (non-existing) neighbor light is always off. 

Write a program that returns the state of the lights after a certain amount 
of seconds. You will be provided with an array that represents the initial 
status of the lights (with 0 and 1 values, 0 being "off" and 1 being "on") 
and an integer that represents the amount of seconds to be elapsed. Return 
an array with the state of the lights after the given seconds elapse. Note 
that even after updating the light state, its previous state is considered 
for updating the state of the other lights. The light states should be 
all updated at the same time.

For example:

boardLights([1, 0, 0, 1, 0, 0, 0, 0], 1)

should return:

[0, 1, 1, 0, 1, 0, 0, 0]
"""

def boardLights(states, s):
    newStates = [0] * len(states)
    while s > 0: 
        for i in range(1, len(states)-1):
            if states[i-1] == 0 and states[i+1] == 0 or states[i-1] == 1 \
            and states[i+1] == 1:
                newStates[i] = 0
            else:
                newStates[i] = 1
        if states[1] == 1: newStates[0] = 1
        else: newStates[0] = 0
        if states[-2] == 1: newStates[-1] = 1
        else: newStates[-1] = 0
        states = newStates[:]
        s -= 1
    return states

print(boardLights([1, 0, 0, 1, 0, 0, 0, 0], 1))# [0, 1, 1, 0, 1, 0, 0, 0]
print(boardLights([1, 1, 0, 0, 1, 1, 1, 1], 2))# [1, 0, 0, 0, 1, 1, 1, 0]

