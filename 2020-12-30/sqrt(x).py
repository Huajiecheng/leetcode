class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        if x == 0:
            return 0
        while left < right:
            mid = (left+right)//2
            if mid*mid >= x:
                right = mid
            else:
                left = mid + 1
        if left*left == x:
            return left
        else:
            return left - 1
        