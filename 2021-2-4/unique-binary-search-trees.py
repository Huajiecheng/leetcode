class Solution:
    def numTrees(self, n: int) -> int:
        count = {0:1,1:1}
        for i in range(2,n+1):
            temp = 0
            for j in range(i):
                temp += count[j]*count[i-j-1]
            count[i] = temp
        return count[n]
            
        