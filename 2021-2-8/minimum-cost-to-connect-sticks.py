class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1: 
            return 0
    
        cost = 0
        heapq.heapify(sticks)
        
        for _ in range(len(sticks) - 1):
            curr_cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, curr_cost)
            cost += curr_cost
        
        return cost 
        