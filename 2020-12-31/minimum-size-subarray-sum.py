class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        temp = 0
        result = len(nums) + 1
        while right < len(nums):
            temp += nums[right]
            if temp >= s:
                result = min(result, right - left + 1)
                temp -= (nums[left] + nums[right])
                left += 1
            else:
                right += 1
        if result == len(nums) + 1:
            return 0
        else:
            return result
                    
            
            
        