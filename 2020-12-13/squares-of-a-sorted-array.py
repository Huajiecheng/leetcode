class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        r_i = len(nums) - 1
        pos_i = len(nums) - 1
        neg_i = 0
        while pos_i >= neg_i:
            if nums[pos_i]*nums[pos_i] > nums[neg_i]*nums[neg_i]:
                result[r_i] = nums[pos_i]*nums[pos_i]
                pos_i -= 1
            else:
                result[r_i] = nums[neg_i]*nums[neg_i]
                neg_i += 1
            r_i -= 1
        return result