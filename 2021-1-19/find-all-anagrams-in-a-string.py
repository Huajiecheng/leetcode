class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        temp = Counter(s[:len(p)-1])
        result = []
        for i in range(0,len(s)-len(p)+1):
            temp[s[i+len(p)-1]] += 1
            if temp == count:
                result.append(i)
            if temp[s[i]] ==  1:
                del temp[s[i]]
            else:
                temp[s[i]] -= 1
        return result
            