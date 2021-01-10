# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        heven = head.next
        codd = head
        ceven = heven
        while codd.next != None and ceven.next != None:
            codd.next = ceven.next
            codd = codd.next
            ceven.next = codd.next
            ceven = ceven.next
        codd.next = heven
        return head
        
            
            