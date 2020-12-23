class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)-1):
            diff_v = abs(points[i][1] - points[i+1][1])
            diff_h = abs(points[i][0] - points[i+1][0])
            result += max(diff_v,diff_h)
        return result