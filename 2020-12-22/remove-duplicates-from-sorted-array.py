class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        end = 0
        normal = 1
        while end < len(nums) and normal < len(nums):
            if nums[normal] != nums[end]:
                end += 1
                nums[end] = nums[normal]
            normal += 1
        return end + 1