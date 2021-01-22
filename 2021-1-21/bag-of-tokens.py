class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        while l <= r:
            if tokens[l] <= P:
                score += 1
                P -= tokens[l]
                l += 1
            elif score >= 1 and l != r:
                score -= 1
                P += tokens[r]
                r -= 1
            else:
                break
        return score
                
        