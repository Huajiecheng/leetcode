class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        result = 0
        for num in nums:
            if num == 1:
                temp += 1
                if temp > result:
                    result = temp
            else:
                temp = 0
        return result