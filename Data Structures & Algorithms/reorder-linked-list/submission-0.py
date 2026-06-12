# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Beginning of 2nd half of list
        second = slow.next

        # Since slow marks the boundry between the two lists, 
        # We set it to None to represent a tail
        prev = slow.next = None

        # Reverse 2nd half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge tow halfs
        second = prev # After loop is done, prev is set to last node we saw, second is none
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
