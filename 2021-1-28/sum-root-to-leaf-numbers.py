# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        def dfs(prev,curr):
            nonlocal total
            if not curr:
                return
            prev = prev*10 + curr.val
            if not curr.left and not curr.right:
                total += prev
                return            
            dfs(prev,curr.left)
            dfs(prev,curr.right)
        dfs(0,root)
        return total
        