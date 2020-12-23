class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        count = [0] * 1000
        for num in nums:
            count[num-1] += 1
        start = 0
        end = 999
        result = -1
        while start < end:
            if count[start] == 0:
                start += 1
                continue
            if count[end] == 0:
                end -= 1
                continue 
            total = start + end + 2
            if  total >= k: 
                end -= 1
            else:
                start += 1
                if result < total:
                    result = total
        return result