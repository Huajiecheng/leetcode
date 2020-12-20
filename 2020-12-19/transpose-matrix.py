class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = [[0]*len(A) for i in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                B[j][i] = A[i][j]
        return B
                
        