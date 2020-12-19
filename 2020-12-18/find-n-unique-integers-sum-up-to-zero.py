class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0] * n
        value = 1
        if n%2 == 1:
            n -= 1
        for i in range(n):
            if i%2 == 0:
                result[i] = value
            else:
                result[i] = -value
                value += 1
        return result