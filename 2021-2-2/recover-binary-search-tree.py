# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        node = root
        stack = []
        outlier1 = outlier2 = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev and prev.val > node.val:
                    outlier2 = node
                    if not outlier1: 
                        outlier1 = prev
                    else:
                        break
                prev = node
                node = node.right
                
        outlier1.val, outlier2.val = outlier2.val, outlier1.val
        