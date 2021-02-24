class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if(K==1):
            curr = S
            for i in range(0,len(S)):
                temp2 = S[i:]+S[:i]
                if(temp2<curr):
                    curr = temp2
            return curr
        return "".join(sorted(S))
        