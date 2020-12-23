class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while x != 0:
            if x < 0:
                result = result*10 + x%(-10)
            else:
                result = result*10 + x%10   
            x = int(x/10)
        if result < -pow(2,31) or result > (pow(2,31) - 1):
            return 0
        return result