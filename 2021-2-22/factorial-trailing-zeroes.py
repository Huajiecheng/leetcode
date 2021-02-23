class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        factor = 5
        while int(n/factor) >= 1:
            result += int(n/factor)
            factor *= 5
        return result
        