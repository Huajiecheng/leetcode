class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pref = {0:-1}
        result = 0
        temp = 0
        for i in range(len(nums)):
            temp = temp + nums[i]
            if (temp - k) in pref:
                if result < (i - pref[temp - k]):
                    result = i - pref[temp - k]
            if temp not in pref:
                pref[temp] = i
        return result