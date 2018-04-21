
""" bankRequests -- 20min
You've been asked to program a bot for a popular bank that will automate 
the management of incoming requests. There are three types of requests the 
bank can receive:

transfer i j sum: request to transfer sum amount of money from the ith 
account to the jth one;
deposit i sum: request to deposit sum amount of money in the ith account;
withdraw i sum: request to withdraw sum amount of money from the ith account.
Your bot should also be able to process invalid requests. There are two 
types of invalid requests:

invalid account number in the requests;
deposit / withdrawal of a larger amount of money than is currently available.
For the given list of accounts and requests, return the state of accounts 
after all requests have been processed, or an array of a single element 
[-<request_id>] (please note the minus sign), where <request_id> is the 
1-based index of the first invalid request.

Example

For accounts = [10, 100, 20, 50, 30] and
requests = ["withdraw 2 10", "transfer 5 1 20", "deposit 5 20", "transfer 
3 4 15"],
the output should be bankRequests(accounts, requests) = [30, 90, 5, 65, 30].

Here are the states of accounts after each request:

"withdraw 2 10": [10, 90, 20, 50, 30];
"transfer 5 1 20": [30, 90, 20, 50, 10];
"deposit 5 20": [30, 90, 20, 50, 30];
"transfer 3 4 15": [30, 90, 5, 65, 30], which is the answer.
For accounts = [20, 1000, 500, 40, 90] and
requests = ["deposit 3 400", "transfer 1 2 30", "withdraw 4 50"],
the output should be bankRequests(accounts, requests) = [-2].

After the first request, accounts becomes equal to [20, 1000, 900, 40, 90],
but the second one turns it into [-10, 1030, 900, 40, 90], which is invalid. 
Thus, the second request is invalid, and the answer is [-2]. Note that the 
last request is also invalid, but it shouldn't be included in the answer.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer accounts

Array of integers, where accounts[i] is the amount of money in the (i + 1)th 
account.

Guaranteed constraints:
0 < accounts.length ≤ 100,
0 ≤ accounts[i] ≤ 105.

[input] array.string requests

Array of requests in the order they should be processed. Each request is 
guaranteed to be in the format described above.
It is guaranteed that for each i and j in a request 0 < i, j ≤ 1000.

Guaranteed constraints:
0 < requests.length ≤ 100,
for each i, j and sum in each element of request:

0 < i ≤ 1000,
0 < j ≤ 1000,
0 ≤ sum ≤ 105.
[output] array.integer

The accounts after executing all of the requests or array with a single 
integer - the index of the first invalid request preceded by -.
"""

def bankRequests(accs, reqs):
    if not accs or not reqs: return [-1]
    currReq, invalid = [], []
    for i in range(1, len(reqs)+1):
        currReq.extend(reqs[i-1].split())
        if currReq[0] == 'withdraw': calcWith(accs, currReq, invalid)
        elif currReq[0] == 'transfer': calcTrans(accs, currReq, invalid)
        elif currReq[0] == 'deposit': calcDep(accs, currReq, invalid)
        if invalid: return [0-i]
        currReq = []
    return accs

def calcWith(accs, withReq, invalid):
    accWith, amount = int(withReq[1]), int(withReq[2])
    if accWith-1 < len(accs) and accs[accWith-1]-amount >= 0: 
        accs[accWith-1] = accs[accWith-1] - amount
    else: invalid.append(1)

def calcTrans(accs, transReq, invalid):
    accFrom, accTo, amount = int(transReq[1]), int(transReq[2]), int(transReq[3])
    if accFrom-1 < len(accs) and accTo-1 < len(accs) and accs[accFrom-1
    ]-amount >= 0:
        accs[accFrom-1] = accs[accFrom-1] - amount
        accs[accTo-1] = accs[accTo-1] + amount
    else: invalid.append(1)

def calcDep(accs, depReq, invalid):
    accTo, amount = int(depReq[1]), int(depReq[2])
    if accTo-1 < len(accs): accs[accTo-1] = accs[accTo-1] + amount
    else: invalid.append(1)


print(bankRequests([42], ["transfer 1 2 3"])) #[-1]
print(bankRequests([10, 100, 20, 50, 30], ["withdraw 2 10", 
                    "transfer 5 1 20", "deposit 5 20", "transfer 3 4 15"]))
                    #[30, 90, 5, 65, 30]
print(bankRequests([20, 1000, 500, 40, 90], ["deposit 3 400", 
                    "transfer 1 2 30", "withdraw 4 50"])) #[-2]

