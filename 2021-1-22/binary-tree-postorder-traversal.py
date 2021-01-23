# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        while stack or current:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            current = stack.pop()   
            if stack and current.right == stack[-1] :
                stack[-1] = current
                current = current.right
            else:
                result.append(current.val)
                current = None            
        return result
        