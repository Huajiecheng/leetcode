class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix = [0]
        count = 0
        for i in A:
            count += i
            prefix.append(count)
        d = defaultdict(int)
        result = 0
        for i in prefix:
            result += d[i]
            d[i + S] += 1
        return result
        
                
            
        