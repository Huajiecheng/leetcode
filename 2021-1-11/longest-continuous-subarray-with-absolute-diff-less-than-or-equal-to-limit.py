class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_heap, min_heap = deque(), deque()
        l = 0
        for r,v in enumerate(nums):
            while max_heap and nums[max_heap[-1]] < v:
                max_heap.pop()
            max_heap.append(r)

            while min_heap and nums[min_heap[-1]] > v:
                min_heap.pop()
            min_heap.append(r)

            if nums[max_heap[0]] - nums[min_heap[0]] > limit: 
                if max_heap[0] == l:
                    max_heap.popleft()
                if min_heap[0] == l:
                    min_heap.popleft()
                l += 1
        return len(nums) - l
               
                
            
        