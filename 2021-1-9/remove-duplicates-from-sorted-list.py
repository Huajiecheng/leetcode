# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        curr = head.next
        prev = head
        while curr != None:
            if prev.val != curr.val:               
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        return head
        