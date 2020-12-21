class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:        
        result = [0] *(2*n)
        for i in range(0,2*n,2):
            result[i] = nums[int(i/2)]
            result[i+1] = nums[n+int(i/2)]
        return result