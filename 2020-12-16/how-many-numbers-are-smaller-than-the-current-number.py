class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        L_count = [0] * 101
        for num in nums:
            L_count[num] += 1
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            for j in range(num):
                result[i] += L_count[j]
        return result
            