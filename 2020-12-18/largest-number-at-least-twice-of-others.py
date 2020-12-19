class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n1 = -1
        n2 = -1
        n1_i = 0
        for i,num in enumerate(nums):
            if num > n1:
                n2 = n1
                n1 = num
                n1_i = i
            elif num > n2:
                n2 = num
        if n2*2 <= n1:
            return n1_i
        else:
            return -1