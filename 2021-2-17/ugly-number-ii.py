class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        
        for _ in range(n - 1):
            n2 = dp[i2] * 2
            n3 = dp[i3] * 3
            n5 = dp[i5] * 5
            
            n = min(n2, n3, n5)
            dp.append(n)
            
            if n == n2:
                i2 += 1
            if n == n3:
                i3 += 1
            if n == n5:
                i5 += 1
        return dp[-1]
        