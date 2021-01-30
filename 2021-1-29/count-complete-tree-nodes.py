# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_mid(self,root,i,level):
        l, r = 0, 2**level - 1
        for _ in range(level):
            mid = l + (r-l)//2
            if i <= mid:
                root = root.left
                r = mid
            else:
                root = root.right
                l = mid + 1
        return root!=None
        
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        curr = root
        result = 0
        level = 0
        while curr.left:
            level += 1
            curr = curr.left
        result = 2**level - 1
        l, r = 0, result + 1
        n = r
        while l < r:
            mid = l + (r-l)//2
            if not self.find_mid(root,mid,level):
                r = mid
            else:
                l = mid + 1
        return result + l
                
        
        
        