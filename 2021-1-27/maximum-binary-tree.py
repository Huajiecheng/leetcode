# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not A:
            return None
        stack = []
        for num in A:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
    '''
        def helper(l, r):
            if l == r:
                return None
            maxi = l
            for i in range(l,r):
                if nums[i] > nums[maxi]:
                    maxi = i
            root = TreeNode(nums[maxi])
            root.left = helper(l,maxi)
            root.right = helper(maxi+1,r)
            return root
        return helper(0, len(nums))
    '''
        
        