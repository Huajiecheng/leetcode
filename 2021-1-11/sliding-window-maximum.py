class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = deque()
        l = 0
        for r,v in enumerate(nums):
            while max_heap and nums[max_heap[-1]] < v:
                max_heap.pop()
            max_heap.append(r)

            if r - l + 1 > k: 
                if max_heap[0] == l:
                    max_heap.popleft()
                l += 1
            if r - l + 1 == k:
                result.append(nums[max_heap[0]])           
        return result
        