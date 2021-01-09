class Solution:
    def findgcd(self, a,b):
        if a < b:
            a, b = b, a
        while b!=0:
            a, b = b, a%b
        return a
    
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for i in range(2,n+1):
            for j in range(1,i):
                if self.findgcd(i,j) == 1:
                    result.append(str(j)+"/"+str(i))
        return result
            
            
        
        
        