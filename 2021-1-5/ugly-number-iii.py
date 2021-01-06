def findlcm(a,b):
    maxn = 2*(10**9)
    if a < b: 
        num1, num2 = b, a
    else:
        num1, num2 = a, b        
    while num2 != 0: 
        num1, num2 = num2, num1 % num2
    if a//num1 > maxn//num1:
        return maxn
    else:
        return a*b//num1
    
def uglybelow(k,a,b,c,l1,l2,l3,l4):
    return k//a + k//b + k//c - k//l1 - k//l2 - k//l3 + k//l4
       
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l1 = findlcm(a,b)
        l2 = findlcm(a,c)
        l3 = findlcm(b,c)
        l4 = findlcm(l1,c)
        left, right = 1, 2*(10**9)
        while left < right:
            mid = (left+right)//2
            if uglybelow(mid,a,b,c,l1,l2,l3,l4) >= n:
                right = mid
            else:
                left = mid + 1
        return left
        
        
        
        