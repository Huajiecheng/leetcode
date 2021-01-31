# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        count = []
        def dfs(curr):
            if not curr:
                return 0
            level = 1 + max(dfs(curr.left),dfs(curr.right))
            if level > len(count):
                count.append([])
            count[level-1].append(curr.val)
            return level
        dfs(root)
        return count
        