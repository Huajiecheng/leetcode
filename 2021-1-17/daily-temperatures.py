class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0]*len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                p = stack.pop()
                result[p] = i - p
            stack.append(i)
        return result
            
        