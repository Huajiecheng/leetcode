class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        count = [-1]*len(nums)
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                count[stack.pop()] = num
            stack.append(i)
        for num in nums:
            while stack and num > nums[stack[-1]]:
                count[stack.pop()] = num
        return count
        