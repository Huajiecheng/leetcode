class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        val, ct = 1, 8
        for i in range(2, n):
            val *= ct
            ct -= 1
        return 81 * val + self.countNumbersWithUniqueDigits(n - 1)