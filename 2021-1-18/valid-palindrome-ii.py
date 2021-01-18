class Solution:
    def pali(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.pali(s[l+1:r+1]) or self.pali(s[l:r])
            l += 1
            r -= 1
        return True
                
                