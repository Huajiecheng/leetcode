# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = head
        new_head = prev.next
        prev.next = new_head.next
        new_head.next = prev        
        while prev.next != None and prev.next.next != None:
            curr = prev.next
            next_n = curr.next
            curr.next = next_n.next
            prev.next = next_n
            next_n.next = curr 
            prev = curr
        return new_head
        