class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(B[0])
        t = len(A[0])
        
        res = [[0]*m for row in range(0, n)]

        for i in range(0, n):
            for k in range(0, t):
                if A[i][k] == 0:
                    continue
                for j in range(0, m):
                    if B[k][j] == 0:
                        continue
                    res[i][j] += A[i][k] * B[k][j]
                    
        return res