class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9 + 7
        stack = []
        arr = [0]+arr+[0]
        result = 0
        for i,v in enumerate(arr):
            while stack and arr[stack[-1]] > v:
                mid = stack.pop()
                l = stack[-1]
                result = (result + arr[mid]*(mid-l)*(i-mid))%modulo
            stack.append(i)
        return result
                
            
        