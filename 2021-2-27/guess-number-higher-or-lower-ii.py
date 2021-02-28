class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
        for offset in range(1,n+1):
            for a in range(n+1-offset):
                b = a+offset
                dp[a][b] = min([max(dp[a][k-1],dp[k+1][b])+k for k in range(a,b)])
        return dp[1][-1]
        