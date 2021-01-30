class Solution:
    def integerReplacement(self, n: int) -> int:
        record = {}    
        def dfs(count,n):
            if n == 1:
                return count
            if n not in record:
                if n%2 == 0:
                    record[n] = dfs(1,n//2)
                else:
                    record[n] = min(dfs(1,n-1),dfs(1,n+1))  
            return count + record[n]
        return dfs(0,n)
    
               
                
        