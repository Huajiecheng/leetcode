class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for k,v in count.items():
            if v == 1:
                return k
        