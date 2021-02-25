class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        curr_max = A[0]
        for i in range(len(A)-2):
            curr_max = max(curr_max, A[i])
            if curr_max >= A[i+2]:
                return False
        return True
        