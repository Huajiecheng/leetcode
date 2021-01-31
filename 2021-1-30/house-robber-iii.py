# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(curr):
            if not curr:
                return 0, 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            rob = curr.val + l[1] + r[1]
            n_rob = max(l) + max(r)
            return rob, n_rob
        return max(dfs(root))
        
        