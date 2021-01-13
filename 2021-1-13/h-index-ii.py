class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        left, right = 0, len(citations) - 1
        while left < right:
            mid = left + (right - left)//2
            if citations[mid] >= len(citations) - mid:
                right = mid
            else:
                left = mid + 1
        if citations[left] >= len(citations) - left:
            return len(citations) - left
        else:
            return 0
            
        