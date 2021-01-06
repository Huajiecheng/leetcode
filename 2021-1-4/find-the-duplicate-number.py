class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0] 
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        head = nums[0]
        while head != slow:
            slow = nums[slow]
            head = nums[head]
        return head
            