class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weight = []
        self.cum = 0
        
        for rect in rects:
            x1, y1, x2, y2 = rect
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.cum += area
            self.weight.append(area)

    def pick(self) -> List[int]:
        u = random.random() * self.cum
        i = 0
        while self.weight[i] < u:
            u -= self.weight[i]
            i += 1
        x1, y1, x2, y2 = self.rects[i]
        
        return [int(u) % (x2 - x1 + 1) + x1, int(u) // (x2 - x1 + 1) + y1]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()