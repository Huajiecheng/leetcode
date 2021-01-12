class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = defaultdict(int)
        result = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while len(count) >= 3:
                if count[s[l]] == 1:
                    del count[s[l]]
                else:
                    count[s[l]] -= 1
                l += 1
            result += r - l + 1
        return len(s)*(len(s)+1)//2 - result
        