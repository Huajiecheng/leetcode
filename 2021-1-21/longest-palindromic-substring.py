class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '$#' + '#'.join(list(s)) + '#*'
        n = len(t)
        p = [0] * n
        c = r = cm = rm = 0
        for i in range(1, n-1):
            p[i] = min(p[2*c-i], r-i) if i < r else 1
            while t[i-p[i]] == t[i+p[i]]: 
                p[i] += 1 
            if p[i] > rm: 
                cm, rm = i, p[i]
            if i+p[i] > r: 
                c, r = i, i+p[i]
        return s[(cm-rm)//2:(cm+rm-1)//2]
'''
    def findP(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - l - 1
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        l = 0
        r = 0
        for i in range(len(s)):
            p1 = self.findP(s,i,i)
            p2 = self.findP(s,i,i+1)
            if p1[1] > p2[1]:
                p = p1
            else:
                p = p2
            if p[1] > r - l:
                l = p[0]
                r = p[0] + p[1] - 1
        return s[l:r+1]
'''
    
            
            
        
        
        
        