
""" coinChange
Given a coin list and a desired change, calculate the minimum amount of
coins to give to make the exact change, and also return the coins used. 
Assume that it is always possible to make the change (or one of the coins 
is 1 cent)
"""

def coinChange(coinList,change):
    minCoins, coinsTable = [0]*(change+1), [0]*(change+1)
    for chng in range(change+1):
        coinNumber = chng
        newCoin = coinList[0]
        for coinUnit in [c for c in coinList if c <= chng]:
            if minCoins[chng-coinUnit] + 1 < coinNumber:
                coinNumber = minCoins[chng-coinUnit] + 1
                newCoin = coinUnit
        minCoins[chng], coinsTable[chng] = coinNumber, newCoin
    coinsUsed, chngLeft = [], change
    while chngLeft > 0:
        thisCoin = coinsTable[chngLeft]
        coinsUsed.append(thisCoin)
        chngLeft = chngLeft - thisCoin  
    return (minCoins[change], coinsUsed)

# assuming that coinList (1st argument) is ordered
print(coinChange([1,5,10,21,25],63)) #(3, [21, 21, 21])
print(coinChange([1,5,10,21,25],17)) #(4, [1, 1, 5, 10])
print(coinChange([1,5,10,21,25],178)) #(9, [1, 10, 21, 21, 25, 25, 25, 25, 25])


