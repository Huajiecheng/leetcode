class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        temp = sum(arr[:k])
        limit = k * threshold
        if temp >= limit:
            count += 1
        for r in range(k,len(arr)):
            temp += arr[r] - arr[r-k]
            if temp >= limit:
                count += 1
        return count
        