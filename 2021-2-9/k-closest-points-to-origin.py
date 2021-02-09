class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        d = {}
        for i,p in enumerate(points):
            dist = (p[0]*p[0]+p[1]*p[1])
            d[i] = dist
        sorted_dist = sorted(d, key = d.get)
        for i in sorted_dist:
            if K>0:
                res.append(points[i])
                K-=1
        return res
        