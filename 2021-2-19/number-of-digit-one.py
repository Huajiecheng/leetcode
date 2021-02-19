class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        result = 0
        while n >= digit:
            q = n//digit
            r = n%digit
            result += (q+8)//10*digit+(q%10==1)*(r+1)
            digit*=10
        return result
            
        