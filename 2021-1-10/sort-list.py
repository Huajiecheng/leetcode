# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l, r):
        dummy = ListNode(-1)
        curr = dummy
        while l != None and r != None:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        if l == None:
            curr.next = r
        else:
            curr.next = l
        return dummy.next
                         
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
        