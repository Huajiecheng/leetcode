class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left1, left2 = 0, 0
        count= 0
        result = 0
        for i, num in enumerate(nums):
            if num%2:
                count += 1
    
            while left1 < i and count > k:
                if nums[left1]%2:
                    count -= 1
                left1 += 1
                
            if count == k:
                left2 =  left1
                while left2 < i and not nums[left2]%2:
                    left2 += 1
                result += (left2-left1+1)
                
        return result
            
                
            
            
        