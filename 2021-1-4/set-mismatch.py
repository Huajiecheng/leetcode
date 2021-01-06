class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        total = sum(nums)
        for num in nums:
            if (nums[abs(num) - 1]<0):
                dup = abs(num)
                break
            nums[abs(num)-1] = -nums[abs(num)-1]            
        miss = (1+len(nums))*len(nums)//2 - (total - dup)
        return [dup, miss]
        