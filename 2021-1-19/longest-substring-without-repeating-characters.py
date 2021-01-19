class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        result = 0
        for i in range(len(s)):
            if s[i] in count:
                l = max(l,count[s[i]] + 1)
            count[s[i]] = i 
            result = max(result, i-l+1)
        return result
            
        
        