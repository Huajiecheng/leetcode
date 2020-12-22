class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(M[0]) for i in M]
        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 0
                total = 0
                for p in range(i-1,i+2):
                    for q in range(j-1,j+2):
                        if 0 <= p < len(M) and 0<= q < len(M[0]):
                            total += M[p][q]
                            count += 1
                result[i][j] = int(total/count)
        return result
        