# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        freq = 0
        pre = None
        cnt = 0
        
        def inorder(node):
            if not node:
                return
            nonlocal ans, freq, pre, cnt
            if node.left:
                inorder(node.left)
            if node.val == pre:
                cnt += 1
            else:                
                cnt = 1
            if cnt == freq:
                ans.append(node.val)
            elif cnt > freq:
                freq = cnt
                ans = [node.val]
            pre = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return ans