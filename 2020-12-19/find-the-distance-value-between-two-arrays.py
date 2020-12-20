class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        p1 = 0
        p2 = 0
        result = len(arr1)
        while p1 < len(arr1) and p2 < len(arr2):
            if abs(arr1[p1] - arr2[p2]) <= d:
                result -= 1
                p1 += 1
            elif arr1[p1] > arr2[p2]:
                p2 += 1
            else:
                p1 += 1
        return result
        