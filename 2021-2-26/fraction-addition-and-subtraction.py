class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall('[+-]?\d+', expression)))
        A, B = 0, 1
        for i in range(0,len(nums),2):
            a, b = nums[i], nums[i+1]            
            A = A * b + a * B
            B *= b            
            t = math.gcd(A, B)            
            A //= t
            B //= t
        return str(A)+"/"+str(B)
        