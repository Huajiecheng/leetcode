# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        flag = False
        while q:
            n = len(q)
            temp = []
            for _ in range(n):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if flag:
                result.append(reversed(temp))
            else:
                result.append(temp)
            flag = not flag              
        return result
        