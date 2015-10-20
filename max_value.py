# Given a sequence of n real numbers, determine a contiguous subsequence 
# for which the sum of elements in the subsequences is maxmized.

arr = [1, 2, 3, 3, 3, 120, -4, -5, 8, 9, 100, -500, 20, 60, -100, 101]

from collections import namedtuple

# beg: the beginning of the subsequence
# end: the end of the subsequence
# sum: the sum of the subsequence

Node = namedtuple('Node', ['beg', 'end', 'sum'])

def sequence(arr):
    max_node = Node(beg=None, end=None, sum=float('-inf'))
    table = []

    for i, e in enumerate(arr):
        if i == 0:
            table.append(Node(beg=i, end=i, sum=e))
        else:
            node = table[i - 1] # optimal sequence that ending at i - 1 position 
            new_node = Node(beg=i, end=i, sum=e) if e > node.sum + e else Node(beg=node.beg, end=i, sum=node.sum + e)
            table.append(new_node)

        if table[i].sum > max_node.sum:
            max_node = table[i]

    return max_node, table



node, _ = sequence(arr)

print(arr[slice(node.beg, node.end + 1)])
input()