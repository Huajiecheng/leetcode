class Solution:

    def __init__(self, w: List[int]):        
        accu = 0      
        self.weights = []        
        for i in w:
            accu += i
            self.weights.append(accu)        

    def pickIndex(self) -> int:        
        p = random.random() * self.weights[-1]
        
        left = 0
        right = len(self.weights)
        
        while left < right:
            mid = (left + right) // 2
            if p <= self.weights[mid]:
                right = mid
            else:
                left = mid + 1
                
        return left
