class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        prev_status = ""
        curr_status = ""
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                curr_status = "i"
            elif A[i] > A[i+1]:
                curr_status = "d"
            else:
                continue
            if prev_status != "" and curr_status != prev_status:
                return False
            prev_status = curr_status
        return True