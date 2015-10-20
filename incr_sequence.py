# find the maximum increasing sequence

arr = [5, 2, 8, 6, 3, 6, 9, 7, 1, 2, 3, 4, 5, 10, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 20, 35, 30, 40, 50, 60, 77, 70, 85, 80, 90, 100, 1, 2, 3]

from collections import namedtuple
from operator import attrgetter

# Record is a data structure that remember all the predecessor of each element (must be smaller than the elements)
# elem: current element
# prev: all the predecessor of the current element that is smaller than current element
Record = namedtuple('Record', ['elem', 'prev'])

# pos:  current position in the original sequence
# len:  the length of optimal increasing sequence that end at position pos
# prev: previous Nodes in the optimal sequence
Node = namedtuple("Node", ['pos', 'len', 'prev'])

# convert a list to a map generator
# key: position in the original sequence
# value: Record
# example: the 3rd element 8 => {2 : Record(8, [5, 2])}
#          the 4th element 6 => {3 : Record(6, [5, 2])}
def make_map(a):
    r = list(reversed(a))
    l = len(r) - 1

    ret = {l - i : Record(elem = e, prev = [len(r[i + 1:]) - 1 - ii for ii, ee in enumerate(r[i + 1:]) if ee < e]) for i, e in enumerate(r) }
    return ret

# bottom up dynamic programming
# return the last node of maximum sequence and 
# the table that has all the optimal results for 
# each element that is ending.
def make_table(map):
    table = {}
    node = None

    for k, v in map.items():
        if not v.prev:
            cur = Node(pos=k, len=1, prev=None)
        else:
            max_pre = max({table[p] for p in v.prev}, key=attrgetter('len'))
            cur = Node(pos=k, len=1 + max_pre.len, prev=max_pre)

        table[k] = cur
        if node == None or node.len < cur.len:
            node = cur

    return (node, table)

def index(node):
    yield node.pos
    while node.prev:
        node = node.prev
        yield node.pos

def longest(arr):
    map= make_map(arr)
    node, _ = make_table(map)
    return reversed([arr[i] for i in index(node)])

for elem in longest(arr):
    print(elem, end=" ")

input()
