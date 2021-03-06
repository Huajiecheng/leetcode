class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p_a, p_b):
            # Leave distances squared
            return (p_a[0] - p_b[0])**2 + (p_a[1] - p_b[1])**2
        
        point_list = [p1, p2, p3, p4]
        
        distances = defaultdict(int)        
        
        for i in range(0, 4):
            p_a = point_list[i]
            for j in range(0, 4):        
                p_b = point_list[j]
                distances[dist(p_a, p_b)] += 1      
                
        diag = max(distances.keys())

        return (distances[diag] != 0) and (distances[0]==4) and (distances[diag]==4) and (distances[diag]*2==distances[diag//2])