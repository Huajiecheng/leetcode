class Solution:
    def countl(self, nums, k):
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > k:
                left += 1
            count += right - left
        return count
        
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left)//2
            if self.countl(nums,mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
            
        
        
        