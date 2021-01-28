# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []
        def dfs(prev,new):            
            if not prev:
                prev = str(new.val)
            else:
                prev += "->" + str(new.val)
            if not new.left and not new.right:
                result.append(prev)
                return
            if new.left:
                dfs(prev, new.left)
            if new.right:
                dfs(prev, new.right)
        dfs("",root)  
        return result
                
        