class Solution:
    def largeR(self,heights):
        stack = [-1]
        heights.append(0)
        result = 0
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                h = heights[stack.pop()]
                l = i - stack[-1] - 1
                result = max(result,h*l)
            stack.append(i)
        heights.pop()
        return result
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix),len(matrix[0])
        dp = [0]*n
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[j] = dp[j] + 1
                else:
                    dp[j] = 0
            result = max(result, self.largeR(dp))
        return result
                
                    