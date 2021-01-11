# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev = head
        curr = prev.next
        prev.next = None         
        while curr != None:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        return prev
        