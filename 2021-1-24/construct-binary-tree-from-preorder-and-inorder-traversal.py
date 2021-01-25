# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(i,l,r):
            if l == r:
                return None
            root = TreeNode(preorder[i])
            mid = count[root.val]
            root.left = build(i+1,l,mid)
            root.right = build(i+mid-l+1,mid+1,r)
            return root
            
        count = {}
        for i, v in enumerate(inorder):
            count[v] = i
        return build(0,0,len(inorder))
        
        