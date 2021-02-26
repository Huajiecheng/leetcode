class Solution:
    def titleToNumber(self, s: str) -> int:
        base = 1
        num = 0
        for c in reversed(s):
            n = ord(c) - ord('A') + 1
            num += n * base
            base *= 26
        return num
        