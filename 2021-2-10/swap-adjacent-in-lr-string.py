class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        s = 0
        e = 0
        
        while True:
            
            while s < n and start[s] == 'X':
                s += 1
                
            while e < n and end[e] == 'X':
                e += 1
                
            if s == n or e == n:
                return s == n and e == n
            
            if start[s] != end[e]:
                return False
                
            if start[s] == 'R' and s > e:
                return False
            
            if start[s] == "L" and s < e:
                return False
            
            s += 1
            e += 1
        