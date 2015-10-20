# Given n types of coin denominations of values v(1) < v(2) < .... < v(n)(all integers).
# Assume v(1) = 1, so coin change can always happen. For any given amount of money C.
# Given an algorithm that makes change for an amount of money C with as few coins as possible

from collections import namedtuple
import copy

coins = [1, 5, 10, 25, 50, 100]

def change(amount):
    table = {0 : []} # the length of value is the number of coins
                     # so 0 value doesn't have any changes

    for c in range(1, amount + 1):
        _, coin_value = min((len(table[c - coin]), coin) for coin in coins if c - coin >= 0)   
        arr = copy.deepcopy(table[c - coin_value])
        arr.append(coin_value)
        table[c] = arr

    return table[amount], table

arr, _ = change(90)

print(arr)
input()