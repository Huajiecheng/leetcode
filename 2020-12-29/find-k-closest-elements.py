class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right)//2
            if arr[mid] >= x:
                right = mid
            else:
                left = mid + 1
        i, j = left - 1, left
        count = 0
        while i >= 0 and j < len(arr) and count < k:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
            count += 1
        if j == len(arr):
            return arr[len(arr)-k:]
        else:
            return arr[i+1:i+1+k]