class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        count_even = 0
        for item in A:
            if item%2 == 0:
                count_even += 1
        if count_even == len(A) or count_even == 0:
            return A
        i_even = 0
        i_odd = len(A) - 1
        while i_even < count_even:
            if A[i_even]%2 == 1:
                while i_odd >= count_even:
                    if A[i_odd]%2 == 0:
                        A[i_even], A[i_odd] = A[i_odd], A[i_even]
                        i_odd -= 1
                        break
                    i_odd -= 1
            i_even += 1
        return A