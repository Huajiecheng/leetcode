# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        s_curr = slow.next
        if s_curr == None:
            return True
        s_prev = None
        while s_curr != None:            
            s_next = s_curr.next
            s_curr.next = s_prev
            s_prev = s_curr
            s_curr = s_next                        
        mid.next = s_prev
        start = head
        while s_prev != None:
            if s_prev.val != start.val:
                return False
            s_prev = s_prev.next
            start  = start.next
        return True
        