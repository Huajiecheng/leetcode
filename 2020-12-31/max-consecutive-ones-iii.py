class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        result = 0
        count_k = 0
        while right < len(A):
            if A[right] == 0:
                count_k += 1
            if count_k <= K:
                result = max(result, right - left + 1)
            else:
                if A[left] == 0:
                    count_k -= 1
                left += 1                
            right += 1
        return result

                
            
            
        