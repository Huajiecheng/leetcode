class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        r = 0
        c = len(grid[0]) - 1
        while r < len(grid) and c >= 0:
            if grid[r][c] >= 0:
                r += 1
                count += len(grid[0]) - c - 1
            else:
                c -= 1                                
        count += len(grid[0])* (len(grid) - r)       
        return count