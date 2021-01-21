class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0
        while l < r:
            result = max(result, (r - l)*min(height[l],height[r]))
            if height[l] > height[r]:
                limit = height[r]
                r -= 1
                while r > l and height[r] <= limit:
                    r -= 1
            else:
                limit = height[l]
                l += 1
                while l < r and height[l] <= limit:
                    l += 1
        return result
        