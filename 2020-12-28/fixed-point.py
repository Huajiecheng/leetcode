class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right)//2
            if A[mid] >= mid:
                right = mid
            else:
                left = mid + 1
        if A[left] == left:
            return left
        else:
            return -1