"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
    	if not root:
            return []
        if not root.children:
            return [root.val]
        result = []
        stack = []
        curr = root
        while stack or curr:
            while curr and curr.children:
                for i in range(len(curr.children)-1,0,-1):
                    stack.append(curr.children[i])
                stack.append(curr)
                curr = curr.children[0]
            if curr:
                result.append(curr.val)
            curr = stack.pop()
            node = curr
            if stack and stack[-1] in curr.children:
                curr = stack[-1]
                stack[-1] = node
            else:
                result.append(curr.val)
                curr = None
        return result
        '''
        if not root:
            return None
        result = []
        for i in root.children:
            result += self.postorder(i)
        result.append(root.val)
        return result
        '''
            
        