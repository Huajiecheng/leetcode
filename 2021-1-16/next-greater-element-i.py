class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        count = {}
        result = []
        for num in nums2:
            while stack and num > stack[-1]:
                count[stack.pop()] = num
            stack.append(num)
        while stack:
            count[stack.pop()] = -1
        for num in nums1:
            result.append(count[num])
        return result
                
                
        