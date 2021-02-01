# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(curr,min_v,max_v):
            if not curr:
                return True
            if curr.val <= min_v or curr.val >= max_v:
                return False
            return dfs(curr.left,min_v,curr.val) and dfs(curr.right,curr.val, max_v)             
        return dfs(root,float("-inf"),float("inf"))
        