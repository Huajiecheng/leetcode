class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        result = 0
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                h = heights[stack.pop()]
                l = i - stack[-1] - 1
                result = max(result,h*l)
            stack.append(i)
        return result
         
        
                
        