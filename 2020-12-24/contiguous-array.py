class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pref = {0:-1}
        result = 0
        temp = 0
        for i,num in enumerate(nums):
            if num == 1:
                temp += 1
            else:
                temp -= 1
            if temp in pref:
                if result < (i - pref[temp]):
                    result = i - pref[temp]
            if temp not in pref:
                pref[temp] = i
        return result
        