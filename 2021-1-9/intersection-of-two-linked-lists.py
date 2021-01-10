# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = 0
        l2 = 0
        c1 = headA
        c2 = headB
        while c1 != None:
            l1 += 1
            c1 = c1.next
        while c2 != None:
            l2 += 1
            c2 = c2.next
        c1 = headA
        c2 = headB
        count = 0
        if l1 > l2:
            while count != (l1-l2):
                count += 1
                c1 = c1.next
        else:
            while count != (l2-l1):
                count += 1
                c2 = c2.next
        while c1 != None:
            if c1 == c2:
                return c1
            c1 = c1.next
            c2 = c2.next
        return None
            
        
        
        