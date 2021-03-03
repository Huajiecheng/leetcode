class Solution:

    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        
    def randPoint(self):
        alpha = 2* math.pi * random.random()        
        r = self.radius * math.sqrt(random.random())
        x = r * math.cos(alpha) + self.x_center
        y = r * math.sin(alpha) + self.y_center
        
        return [x, y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()