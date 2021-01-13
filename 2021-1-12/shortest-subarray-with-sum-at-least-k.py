class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        prefix = [0]
        for i in A:
            prefix.append(prefix[-1] + i)
        result = len(A) + 1
        temp = deque()
        for r, v in enumerate(prefix):
            while temp and v <= prefix[temp[-1]]:
                temp.pop()
            while temp and v - prefix[temp[0]] >= K:
                result = min(result,r - temp.popleft())
            temp.append(r)
        if result == len(A) + 1:
            return -1
        else:
            return result
                
            
        