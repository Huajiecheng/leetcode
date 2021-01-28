"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def helper(self, up, curr, start):
        if up:
            if curr:
                curr.next = up
            else:
                start = up
            curr = up
        return curr, start
    
    def connect(self, root: 'Node') -> 'Node':
        start = root
        while start:
            uplevel, curr = start, None
            start = None
            while uplevel:
                curr, start = self.helper(uplevel.left,curr,start)
                curr, start = self.helper(uplevel.right,curr,start)
                uplevel = uplevel.next
        return root
                
            
    '''       
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if i < n - 1:
                    curr.next = q[0]                                    
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)            
        return root
    '''