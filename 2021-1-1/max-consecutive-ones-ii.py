class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        count_k = 0
        result = 0
        while right < len(nums):
            if nums[right] == 0:
                count_k += 1
            if count_k <= 1:
                result = max(result, right - left + 1)
            else:
                if nums[left] == 0:
                    count_k -= 1
                left += 1                   
            right += 1
        return result
            
            
        
        