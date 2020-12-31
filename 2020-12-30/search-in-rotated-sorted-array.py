class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= nums[-1] or nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        if nums[0] <= nums[-1]:
            i, j = 0, len(nums) - 1
        elif target <= nums[-1]:
            i, j = left + 1, len(nums) - 1 
        elif target >= nums[0]:
            i, j = 0, left
        else:
            return -1
        while i <= j:
            mid = (i + j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
            
                
        