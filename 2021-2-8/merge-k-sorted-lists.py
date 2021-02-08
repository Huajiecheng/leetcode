# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                pq.append((lists[i].val, i))
        heapq.heapify(pq)
        
        head = ListNode()
        res = head
        while pq:
            pop = heapq.heappop(pq)
            res.next = lists[pop[1]]
            res = res.next
            if lists[pop[1]].next:
                heapq.heappush(pq, (lists[pop[1]].next.val, pop[1]))
                lists[pop[1]] = lists[pop[1]].next
        return head.next
        