# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        cur = head
        prev = head
        newHead = None

        while cur:
            nxt = cur.next
            if nxt:
                cur.next = nxt.next
                nxt.next = prev
                prev = nxt
            else:
                # tail
                newHead = prev
                break
        
        return newHead
        
