# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, prev,new,s,result):
            if not new:
                return None
            prev.append(new.val) 
            s -= new.val
            if not new.left and not new.right and s == 0:
                result.append(list(prev))
            else:
                self.dfs(prev,new.left, s,result)
                self.dfs(prev,new.right, s,result)
            prev.pop()
            
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []        
        self.dfs([], root, targetSum, result)
        return result