class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l < r:
            mid = l + (r - l)//2
            if self.count(matrix, mid) < k:
                l = mid + 1
            else:
                r = mid                
        return r
    
    def count(self, m, target):
        total = 0        
        row, col = len(m) - 1, 0
        while row >= 0 and col < len(m):
            if m[row][col] <= target:
                total += row + 1
                col += 1
            else:
                row -= 1
        return total
        