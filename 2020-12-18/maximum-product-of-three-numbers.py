class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l1 = l2 = l3 = -1001
        s1 = s2 = 1001
        for num in nums:
            if num > l1:
                l3 = l2
                l2 = l1
                l1 = num
            elif num > l2:
                l3 = l2
                l2 = num
            elif num > l3:
                l3 = num
            if num < s1:
                s2 = s1
                s1 = num
            elif num < s2:
                s2 = num
        return max(l1*l2*l3, s1*s2*l1) 