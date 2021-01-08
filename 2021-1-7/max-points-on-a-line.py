class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        max_count = 0
        same = 1
        same_y = 1
        for i in range(len(points)):
            same = 1
            same_y = 1
            same_x = 1
            for j in range(i+1, len(points)):
                if points[i][1] == points[j][1]:
                    same_y += 1
                    if points[i][0] == points[j][0]:
                        same += 1
                elif points[i][0] == points[j][0]:
                    same_x += 1
                else:
                    dx = points[i][0] - points[j][0]
                    dy = points[i][1] - points[j][1]
                    Gcd = gcd(dx, dy)
                    slope = (dx / Gcd, dy / Gcd)
                    slope = slope if slope[0] >0 else (-slope[0], -slope[1])                    
                    hashmap[slope] += 1
            max_count = max(max_count, same_y, same_x)
            for it in hashmap:
                max_count = max(max_count, same+hashmap[it])
            hashmap.clear()
        return max_count
        