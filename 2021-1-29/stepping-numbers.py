class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        if low > 0:
            result = []
        else:
            result = [0]
        q = deque([])
        for i in range(1,10):
            q.append(i)
        while q:
            curr = q.popleft()
            if curr >= low and curr <= high: 
                result.append(curr)
            if curr < high:
                lastdigit = curr%10
                minus = lastdigit-1
                plus = lastdigit+1
                if minus >= 0:
                    q.append(curr*10+minus)
                if plus < 10 :
                    q.append(curr*10+plus)
        return result
        
                
            
        
        