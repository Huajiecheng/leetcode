class Solution:
    def convertToTitle(self, n: int) -> str:
        x = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        y = ""
        while n>0:
            z = n%26
            if z==0: z=26
            y = x[z]+y
            n = int((n-z)/26)
        return y
        