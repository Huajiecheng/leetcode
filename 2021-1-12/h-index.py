class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0]*(len(citations)+1)
        for i,v in enumerate(citations):
            if v <= len(citations):
                count[v] += 1
        for i in range(1,len(count)):
            count[i] = count[i] + count[i-1]
            if len(citations) - count[i-1] >= i and len(citations) - count[i] <= i:
                return i
        return 0
            
            
        