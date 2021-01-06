class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return False
        half = (len(nums)-1)//2
        if left <= half and nums[left+len(nums)//2] == target:
            return True
        return False
            
        