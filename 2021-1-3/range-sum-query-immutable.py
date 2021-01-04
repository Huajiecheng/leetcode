class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        count = 0
        for i, num in enumerate(nums):
            count += num
            self.prefix.append(count)
        
        

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j+1] - self.prefix[i]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)