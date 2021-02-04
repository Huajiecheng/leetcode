# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_v = min(p.val,q.val)
        max_v = max(p.val,q.val)
        if root.val >= min_v and root.val <= max_v:
            return root
        elif root.val < min_v:
            return self.lowestCommonAncestor(root.right,p,q) 
        elif root.val > max_v:
            return self.lowestCommonAncestor(root.left,p,q)
            
        
        