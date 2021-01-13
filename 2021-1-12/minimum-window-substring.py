class Solution:  
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        temp = Counter()
        limit = len(count)
        reach = 0
        r_size = len(s) + 1
        r_start = 0
        l = 0
        for r,v in enumerate(s):
            temp[v] += 1
            if v in count and temp[v] == count[v]:
                reach += 1
            while reach == limit:
                if r - l + 1 < r_size:
                    r_size = r - l + 1
                    r_start = l
                if s[l] in count and temp[s[l]] == count[s[l]]:
                    reach -= 1
                temp[s[l]] -= 1
                l += 1
        if r_size == len(s) + 1:
            return ""
        else:
            return s[r_start:r_start+r_size]
                    
                
            
        