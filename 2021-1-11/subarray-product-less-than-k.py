class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count = 0
        left = 0
        temp = 1
        for i in range(len(nums)):
            temp *= nums[i]
            while temp >= k:
                temp //= nums[left]
                left += 1
            count += i - left + 1
        return count
                
            
        