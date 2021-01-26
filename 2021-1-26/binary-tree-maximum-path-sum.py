# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:   
        result = float("-inf")
        def dfs(curr):
            nonlocal result
            if not curr:
                return 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            result = max(result, curr.val + l, curr.val + r, curr.val + l + r)
            return max(0, curr.val + r, curr.val + l)        
        dfs(root)
        return result
        
            
        