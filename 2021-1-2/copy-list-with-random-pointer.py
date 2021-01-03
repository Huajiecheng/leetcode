"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        start = head
        result = Node(0)
        copy = result
        count1 = {}
        count2 = {}
        p = 0
        while start.next != None:
            copy.val = start.val
            copy.next = Node(0)
            copy.random = None
            count1[start] = p 
            count2[p] = copy 
            copy = copy.next
            start = start.next
            p += 1
        copy.val = start.val
        count1[start] = p
        count2[p] = copy
        
        start = head
        copy = result
        while start != None:
            if start.random != None:
                index = count1[start.random]
                copy.random = count2[index]
            else:
                copy.random = None
            copy = copy.next
            start = start.next
        return result
        