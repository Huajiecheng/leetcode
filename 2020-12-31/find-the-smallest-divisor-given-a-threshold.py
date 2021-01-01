def find_sum(nums, d):
    count = 0
    for num in nums:
        count += ceil(num/d)
    return count    
    
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left+right)//2
            if find_sum(nums,mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
                
        