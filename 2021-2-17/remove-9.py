class Solution:
    def newInteger(self, n: int) -> int:
        ans = ''
        while n >= 1:
            ans = str(n%9) + ans
            n = n//9
        return int(ans)
        