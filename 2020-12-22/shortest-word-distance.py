class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        result = len(words)
        for i in range(len(words)):
            if word1 == words[i]:
                p1 = i
            elif word2 == words[i]:
                p2 = i
            dis = abs(p2-p1)
            if p1 != -1 and p2 != -1:
                if dis == 1:
                    return 1
                elif result > dis:
                    result = dis
        return result