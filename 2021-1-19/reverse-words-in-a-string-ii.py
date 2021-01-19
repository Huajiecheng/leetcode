class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        s.append(' ')
        l = 0
        for i, c in enumerate(s):
            if c == ' ' or i == len(s) - 1:
                r = i-1
                while l < r:
                    s[l] , s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = i + 1
        s.pop()
        