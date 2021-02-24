class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        factorials = [1]
        for x in range(1,n+1):
            factorials.append(factorials[-1]*x)
        
        out = []
        
        for x in range(n):
            out.append(k//factorials[n-x-1])
            k = k%factorials[n-x-1]
        
        out2 = []
        bruh = [x+1 for x in range(n)]
        
        for x in out:
            out2.append(bruh.pop(x))
        return ''.join([str(x) for x in out2])
        