# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if root is None:
            return []
        
        if(k == 0):
            return []        
        nums = []        
        def inOrder(root):          
            if root is None:
                return            
            inOrder(root.left)
            if(len(nums) < k):
                heapq.heappush(nums,(-abs(target-root.val),root.val))                
            else:
                heapq.heappushpop(nums,(-abs(target-root.val),root.val))               
            inOrder(root.right)                
        inOrder(root)           
        result = []      
        while nums:            
            result.append(nums[0][1])
            heapq.heappop(nums)          
        return result
        