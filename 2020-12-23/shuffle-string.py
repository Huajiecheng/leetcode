class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        count = [""]*100
        for i, indice in enumerate(indices):
            count[indice] = s[i]
        result = "".join(count)
        return result