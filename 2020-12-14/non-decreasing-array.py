class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        pos = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if count > 0:
                    return False                    
                count += 1
                pos = i
        if count == 0 or pos == 0 or pos == (len(nums)-2) or nums[pos-1]<=nums[pos+1] or nums[pos]<=nums[pos+2]:
            return True
        else:
            return False