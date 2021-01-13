class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        temp = Counter(s2[:len(s1)])
        if temp == count:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            temp[s2[r]] += 1
            if temp[s2[l]] == 1:
                del temp[s2[l]]
            else:
                temp[s2[l]] -= 1
            l += 1
            if count == temp:
                return True
        return False
        
        