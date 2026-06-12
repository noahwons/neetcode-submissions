# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # inserts node of val 0 at the beginning
        left = dummy
        right = head

        # increment right while n > 0
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # now shift both pointers until right reaches end of list
        # this positions left pointer 1 behiend the node we want to delete
        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next

        return dummy.next
        

        