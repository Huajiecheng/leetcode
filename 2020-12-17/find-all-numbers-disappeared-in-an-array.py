class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                while nums[nums[i]-1] != nums[i]:
                    p = nums[i]
                    nums[i], nums[p-1] =  nums[p-1], nums[i]
            i += 1
        result = []
        for i, num in enumerate(nums): 
            if num != i + 1:
                result.append(i+1)
        return result