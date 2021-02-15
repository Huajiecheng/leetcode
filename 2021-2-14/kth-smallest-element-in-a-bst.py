# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        i = 0
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            i += 1
            if i == k:
                return root.val           
            root = root.right
        return 0