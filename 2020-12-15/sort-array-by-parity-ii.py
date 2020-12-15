class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i_even = 0
        i_odd = 1
        while i_even <= len(A) - 2:
            if A[i_even]%2 == 1:
                while i_odd <= len(A) - 1:
                    if A[i_odd]%2 == 0:
                        A[i_even], A[i_odd] = A[i_odd], A[i_even]
                        i_odd += 2
                        break
                    i_odd += 2
            i_even += 2
        return A