class Solution:
    def isValid(self, s: str) -> bool:
        l = {'(':')','{':'}','[':']'}
        count = []
        for i in s:
            if i in l:
                count.append(i)
            else:
                if count and l[count[-1]] == i:
                    count.pop()
                else:
                    return False
        return len(count) == 0
            
        