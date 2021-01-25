# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 1
        result = 0
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    result = level
                    break
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if result == level:
                break
            level += 1
        return result
        