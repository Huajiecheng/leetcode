class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0        
        max_v = max(nums)
        digit = 1
        while max_v/digit >= 1:
            count = [[] for i in range(10)]
            for num in nums:
                count[num//digit%10].append(num)
            p = 0
            for i in range(10):
                for j in count[i]:
                    nums[p] = j
                    p += 1
            digit *= 10
        result = 0
        for i in range(len(nums)-1):
            result = max(result, nums[i+1]-nums[i])
        return result