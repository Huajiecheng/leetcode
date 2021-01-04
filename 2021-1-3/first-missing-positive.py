class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        
        if len(nums) == 1:
            return 2
            
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 1
        for i,num in enumerate(nums):
            if abs(num) > 1 and abs(num) <= len(nums):
                nums[abs(num)-1] = -abs(nums[abs(num)-1])
        for i in range(1,len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums) + 1
            
            
        
        