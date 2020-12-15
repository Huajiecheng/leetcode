class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h_range = 100
        count = [0] * (h_range + 1)
        for i in range(len(heights)):
            count[heights[i]] += 1
        p = 0
        result = 0
        for i in range(h_range + 1):
            for j in range(count[i]):
                if heights[p] != i:
                    result += 1
                p += 1
        return result