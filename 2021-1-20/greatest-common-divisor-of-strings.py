class Solution:
    def findgcd(self,a,b):
        if a == 0:
            return b
        else:
            return self.findgcd(b%a,a)
                        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        d = self.findgcd(l1,l2)
        if str1[:d]*(l1//d) == str1 and str1[:d]*(l2//d) == str2:
            return str1[:d]
        else:
            return ""
        
            
        