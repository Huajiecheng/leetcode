class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0]*3 for i in range(3)]
        A = 1
        for move in moves:
            grid[move[0]][move[1]] = A
            A *= -1
        c = [0] * 8
        for i in range(3):
            c[i+3] = sum(grid[i])
            c[6] += grid[i][i]
            c[7] += grid[i][3-i-1]
            for j in range(3):
                c[j] += grid[i][j]
        for check in c:
            if check == 3:
                return "A"
            elif check == -3:
                return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"