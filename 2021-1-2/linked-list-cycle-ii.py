# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        fast = head
        slow = head
        flag = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        if not flag:
            return None
        start = head
        while start != slow:
            start = start.next
            slow = slow.next
        return start
        