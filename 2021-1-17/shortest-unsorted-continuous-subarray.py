class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        left, right = 0, len(nums) - 1
        while left < len(nums) - 1 and nums[left] <= nums[left+1]:
            left += 1
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
        if left > right:
            return 0
        bot, top = min(nums[left:right+1]), max(nums[left:right+1])
        while left >= 0 and nums[left] > bot:
            left -= 1
        while right < len(nums) and nums[right] < top:
            right += 1
        return right - left - 1

'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l, r = len(nums), 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        if r - l > 0:
            return r - l + 1
        else:
            return 0
'''