class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] == nums[mid+1]:
                if (mid-left)%2 == 1:
                    right = mid - 1
                else:
                    left = mid + 2              
            elif nums[mid-1] == nums[mid]:
                if (mid-left-1)%2 == 1:
                    right = mid - 2
                else:
                    left = mid + 1               
            else:
                return nums[mid]
        return nums[left]
        