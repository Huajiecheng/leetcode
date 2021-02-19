class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a == 1:
            return 1
        result = 0
        mul = 1
        for i in range(9,1,-1):
            while a%i == 0:
                a = a//i
                result = mul*i + result
                mul *= 10
        if result > 2**31 - 1 or a!= 1:
            return 0
        else:
            return result
             
        