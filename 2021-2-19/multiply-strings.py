class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': 
            return '0'
        result = 0
        for c1 in num2:
            s=0
            for c2 in num1:
                s=s*10 + (ord(c1)-ord('0'))*(ord(c2)-ord('0'))
            result = result*10 + s
        return str(result)
        