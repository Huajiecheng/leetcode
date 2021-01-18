class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i,h in enumerate(height):
            while stack and height[stack[-1]] < h:
                p = stack.pop()
                if stack:
                    result += (min(h, height[stack[-1]]) - height[p])*(i - stack[-1] -1)
            stack.append(i)
        return result
                
            
        