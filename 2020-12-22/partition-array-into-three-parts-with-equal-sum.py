class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        count = 0
        part = 0
        for i, num in enumerate(A):
            part += num
            if part*3 == total:
                count += 1
                part = 0
            if count == 2:
                if sum(A[i+1:])*3 == total and (i + 1) != len(A):
                    return True
                else:
                    return False
        return False