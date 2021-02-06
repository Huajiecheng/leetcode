# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(l,r):
            if l > r:
                return [None]
            t = []
            for i in range(l,r+1):
                l_t = dfs(l,i-1)
                r_t = dfs(i+1,r)
                for j in l_t:
                    for k in r_t:
                        curr = TreeNode(i)
                        curr.left = j
                        curr.right = k
                        t.append(curr)
            return t
        return dfs(1,n)
            
        
        