class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        prefix = [-1,0]
        for i in range(1,len(B)-1):
            if B[prefix[-1]] == B[i]:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(0)
        left = 0
        for i in A+A:
            while left >= 0 and i != B[left]:
                left = prefix[left]
            left += 1
            if left == len(B):
                return True
        return False
        
        
        