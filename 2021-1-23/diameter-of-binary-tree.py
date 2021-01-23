# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def h(self, root):
        if not root:
            return -1,-1
        l, r = self.h(root.left), self.h(root.right)
        length = max(l[0],r[0]) + 1
        result = max(l[1],r[1],l[0]+r[0]+1)
        return length, result
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.h(root)[1] + 1
        
        
        