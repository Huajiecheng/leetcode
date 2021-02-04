# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        result = root.val
        while root:
            if abs(target-root.val) < abs(result-target):
                result = root.val
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val
        return result
            
        