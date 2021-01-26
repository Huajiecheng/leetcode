# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = defaultdict(int)
        result = []
        def dfs(curr):
            if not curr:
                return ""
            key = str(curr.val) + '-' + dfs(curr.left) + '-' + dfs(curr.right)
            count[key] += 1
            if count[key] == 2:
                result.append(curr)
            return key
        dfs(root)
        return result
        