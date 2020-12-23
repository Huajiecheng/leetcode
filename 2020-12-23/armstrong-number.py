class Solution:
    def isArmstrong(self, N: int) -> bool:
        length = len(str(N))
        y = N
        total = 0
        while N != 0:
            total += pow(N%10,length)
            if total > y:
                return False
            N = int(N/10)
        if total == y:
            return True
        else:
            return False