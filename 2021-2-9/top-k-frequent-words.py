class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        l = list(c.items())
        l.sort(key = lambda x: (-x[1], x[0]))
        return [l[i][0] for i in range(k)]
        