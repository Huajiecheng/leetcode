class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)%p
        if total == 0:
            return 0
        pref = {0:-1}
        result = len(nums)
        temp = 0
        for i in range(len(nums)):
            temp = (temp + nums[i])%p
            if (temp - total)%p in pref:
                if result > (i - pref[(temp - total)%p]):
                    result = i - pref[(temp - total)%p]
            pref[temp] = i
        if result == len(nums):
            return -1
        else:
            return result 