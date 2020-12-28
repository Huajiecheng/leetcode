class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = pow(10,9)+7
        left, right = 0, len(nums) - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result+pow(2, right -left, m))%m
                left += 1
            else:
                right -= 1
        return result 