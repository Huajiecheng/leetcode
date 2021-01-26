"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        count = 0
        for i in tree:
            count += i.val
            for j in i.children:
                count -= j.val
        for i in tree:
            if i.val == count:
                return i
                
        