class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero_pos != i:
                    nums[zero_pos] = nums[i]
                    nums[i] = 0
                zero_pos += 1