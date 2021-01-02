class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = {}
        left, right = 0, 0
        result = 0
        while right < len(s):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            if len(count) <= k:
                result = max(result,right - left + 1)
            else:                
                if count[s[left]] == 1:
                    count.pop(s[left])
                else:
                    count[s[left]] -= 1
                left += 1
            right += 1
        return result
            
        