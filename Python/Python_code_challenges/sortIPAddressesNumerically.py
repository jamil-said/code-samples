""" sortIPAddressesNumerically
Given a list of strings with ip addresses, return a list of strings of ip addresses sorted numerically 
"""

def sort_ip(arr):
    temp, res = [], []
    for i in arr:
        temp.append([int(x) for x in i.split('.')])
    temp.sort()
    for i in temp:
        res.append('.'.join([str(x) for x in i]))
    return res

print(sort_ip(['100.10.0.1', '10.9.1.8', '12.30.10.10', '255.1.1.1', '1.1.1.1', '10.9.0.11']))
#['1.1.1.1', '10.9.0.11', '10.9.1.8', '12.30.10.10', '100.10.0.1', '255.1.1.1']

