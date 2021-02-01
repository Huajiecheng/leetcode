# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        result = 0
        def dfs(curr,max_v,min_v):
            nonlocal result
            if not curr:
                return 
            result = max(result,abs(curr.val-max_v),abs(curr.val-min_v))
            max_v, min_v = max(curr.val,max_v),min(curr.val,min_v)
            dfs(curr.left,max_v,min_v)
            dfs(curr.right,max_v,min_v)
        dfs(root, root.val, root.val)
        return result
        