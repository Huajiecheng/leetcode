class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        bottom = nums[0]
        for num in nums:
            s += num
            if s < bottom:
                bottom = s
        if bottom < 0:
            return 1 - bottom
        else:
            return 1