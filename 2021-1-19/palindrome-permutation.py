class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd = 0
        for k, v in count.items():
            if v%2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True
        