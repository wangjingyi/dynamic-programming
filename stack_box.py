# For a set of n types of rectanglar 3-D boxes, where ith box has height h(i), width w(i) and depth d(i). 
# Try to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box
# if the dimension of the 2-D base of lower box are each strctly larger than those of the 2-D base of the higher box.
# Of course, you can rotate a box so that any side functions as its base. It is also allowable to use multiple instance
# of the same type of box.

from collections import namedtuple
from itertools import permutations
#import copy


Box = namedtuple("Box", ['width', 'depth', 'height'])

Node = namedtuple("Node", ['box', 'prev_node', 'max_height'])

arr = [Box(1, 2, 3), Box(2, 5, 8), Box(3, 3, 15), Box(4, 5, 8), Box(5, 10, 12)]

# expand one box to 6 boxes so we don't need deal with rotation problem
def expand(boxes): 
    return [Box(*t) for b in boxes for t in permutations(tuple(b))]

# sort the boxes according to their area
def sort_box(boxes): 
    #cp = copy.deepcopy(boxes)
    boxes.sort(key = lambda b: b.width * b.depth)
    return boxes

# reorganize make one box to 6 boxes and sort the entire
# boxes by their area
def reorganize(boxes): 
    expand_boxes = expand(boxes)
    return sort_box(expand_boxes)

def max_height(boxes):
    table = []
    max_node = Node(None, None, float('-inf'))

    add_itself = lambda box: Node(box = box, prev_node = None, max_height = box.height)

    for i, e in enumerate(boxes):
        if i == 0:
            table.append(add_itself(e))
        else:
            # find all the prev nodes that has smaller width and smaller depth
            prev_nodes = [table[index] for index, box in enumerate(boxes[:i]) if box.width < e.width and box.depth < e.depth]
            if prev_nodes: # not an empty list
                n = max(prev_nodes, key=lambda node: node.max_height)
                table.append(Node(box = e, prev_node = n, max_height = e.height + n.max_height))
            else:
                table.append(add_itself(e))

        if table[i].max_height > max_node.max_height:
            max_node = table[i]

    return max_node, table

def index(node):
    yield node.box
    while node.prev_node:
        node = node.prev_node
        yield node.box

def test(boxes):
    bs = reorganize(boxes)
    max_node, _ = max_height(bs)
    return index(max_node)

for b in test(arr):
    print(b, end=' ')

input()