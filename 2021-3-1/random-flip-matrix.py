class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.seen = set()
        self.n_rows = n_rows
        self.n_cols = n_cols

    def flip(self) -> List[int]:
        while True:
            n = random.randint(0, self.n_rows * self.n_cols - 1)
            if n in self.seen:
                continue
            self.seen.add(n)                
            return [n // self.n_cols, n % self.n_cols]

    def reset(self) -> None:
        self.seen = set()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()