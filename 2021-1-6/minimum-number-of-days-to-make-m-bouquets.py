class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            count = 0
            temp = 0
            for b in bloomDay:
                if b <= mid:
                    temp += 1
                else:
                    count += temp//k
                    temp = 0
            count += temp//k            
            if count >= m:
                right = mid
            else:
                left = mid + 1
        return left