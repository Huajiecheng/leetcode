class Solution:
    def findP(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        l = 0
        r = 0
        for i in range(len(s)):
            p1 = self.findP(s,i,i)
            p2 = self.findP(s,i,i+1)
            p = max(p1,p2)
            if p > r - l:
                l = i - (p-1)//2
                r = i + p//2
        return s[l:r+1]
            
            
        
        
        
        