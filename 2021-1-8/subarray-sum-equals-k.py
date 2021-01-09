class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        result = 0
        count = 0
        for num in nums:
            count += num
            if (count-k) in prefix:
                result += prefix[count-k]
            prefix[count] += 1
        return result
                    
        