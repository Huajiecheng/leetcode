class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        q = []
        
        queue = deque()
        
        for val in nums:
            count = 0
 
            while queue and queue[0][0] + 1 < val:
                _, poppedCount = queue.popleft()
                if poppedCount < 3: return False
            if queue and queue[0][0] + 1 == val:
                _, count = queue.popleft()
            if count == 0:
                queue.appendleft((val, 1))
            else:
                queue.append((val, count + 1))
            
            
        return all(abs(count) >= 3 for _, count in queue)
                

        