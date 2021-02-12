class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        count = []
        for i in range (len(arr)):
            heapq.heappush(count, (arr[i]/arr[-1], i, len(arr)-1))
            
        for i in range (k):
            v, l, r = heapq.heappop(count)
            if r > 0: 
                heapq.heappush(count, (arr[l]/arr[r-1], l, r-1))
        
        return [arr[l],arr[r]]
        
        