class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        count = defaultdict(int)
        left = 0
        for i in range(len(s)):
            count[s[i]] += 1
            maxv = max(count.values())
            if i-left+1 - maxv > k:
                count[s[left]] -= 1
                left += 1
        return i - left + 1
            
            
        