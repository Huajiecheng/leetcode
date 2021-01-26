# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                r = curr.left
                while r.right:
                    r = r.right
                r.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
    '''
    def helper(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        end1 = self.helper(root.left)
        end2 = self.helper(root.right)
        if end1:
            end1.right = root.right
            root.right = root.left
            root.left = None
        if end2:
            return end2
        else:
            return end1
                
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    '''
        
        