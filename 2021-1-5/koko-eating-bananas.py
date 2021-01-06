class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            count = 0
            mid = left + (right-left)//2
            for pile in piles:
                count += ceil(pile/mid)
            if count <= H:
                right = mid
            else:
                left = mid + 1
        return left