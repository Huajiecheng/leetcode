class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.count = deque()
        
        

    def next(self, val: int) -> float:
        if len(self.count) == self.size:
            self.sum = self.sum - self.count[0] + val
            self.count.popleft()
            self.count.append(val)
        else:
            self.sum += val
            self.count.append(val)
        return self.sum/len(self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)