class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sumdict = defaultdict(int)
        sumdict[0] = 1
        count = 0
        for a in A:
            count += a
            sumdict[count%K] += 1
        result = 0
        for v in sumdict.values():
            result += v*(v-1)//2
        return result
        
            
            
            
            
        