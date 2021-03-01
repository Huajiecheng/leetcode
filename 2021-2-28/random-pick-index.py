class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def gen_num(self, n):
        return random.randint(0, n)

    def pick(self, target: int) -> int:
        lst = []
        
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                lst.append(i)
        
        return lst[self.gen_num(len(lst) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)