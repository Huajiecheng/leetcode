class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def reach(a):
            count = 0
            for i in range(1,m+1):
                count += min(a//i,n)
            return count
            
        l, r = 1, m*n
        while l < r:
            mid = l + (r-l)//2
            if reach(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l
        
        
        