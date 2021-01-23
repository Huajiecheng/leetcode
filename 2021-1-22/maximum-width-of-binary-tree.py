# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        result = 0
        q = deque([(root,0)])
        while q:
            n = len(q)
            start = q[0][1]
            for _ in range(n):
                current, index = q.popleft()
                if current.left:
                    q.append((current.left,2*index))
                if current.right:
                    q.append((current.right,2*index+1)) 
            result = max(result,index-start+1)
        return result
            
        