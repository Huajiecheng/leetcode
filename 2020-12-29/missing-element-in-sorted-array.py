class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        s, l = nums[0], nums[right]
        length = len(nums)
        if k > (l - s - length + 1):
            return k + s + length - 1            
        while left < right:
            mid = (left+right)//2
            miss = nums[mid] - s - mid
            if miss >= k:
                right = mid
            else:
                left = mid + 1
        return k + s + left - 1