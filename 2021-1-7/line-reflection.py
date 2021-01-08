class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if len(points) == 1: 
            return True        
        pointSet = set(map(tuple,points))
        maxX = max(points, key=lambda x:x[0])[0]
        minX = min(points, key=lambda x:x[0])[0]
        line = maxX+minX
        for x,y in pointSet:
            if not (line-x, y) in pointSet:
                return False
        return True
        
        