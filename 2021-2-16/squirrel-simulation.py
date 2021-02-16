class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        tree_nut_dists = []
        max_diff = float('-inf')
        
        for x, y in nuts:
            tree_dist = abs(x - tree[0]) + abs(y - tree[1])
            squir_dist = abs(x - squirrel[0]) + abs(y - squirrel[1])
            tree_nut_dists.append(tree_dist)
            
            if tree_dist - squir_dist > max_diff:
                max_diff = tree_dist - squir_dist
        
        return 2 * sum(tree_nut_dists) - max_diff