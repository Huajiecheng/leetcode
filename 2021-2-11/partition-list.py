# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        small = ListNode()
        large = ListNode()
        ps = small
        pl = large
        while head:
            if head.val < x:
                ps.next = head
                ps = head
            else:
                pl.next = head
                pl = head
            head = head.next
        ps.next = large.next
        pl.next = None
        return small.next
        