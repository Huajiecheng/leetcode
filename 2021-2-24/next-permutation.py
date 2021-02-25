class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_max = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[cur_max]:
                for j in range(cur_max+1,len(nums)):
                    if nums[i]<nums[j]<nums[cur_max]: cur_max = j
                nums[i],nums[cur_max]=nums[cur_max],nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return 
            cur_max = i
        
        nums.sort()
        