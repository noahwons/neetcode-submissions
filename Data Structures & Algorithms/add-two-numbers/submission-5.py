# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = ListNode()
        cur3 = dummy
        while cur1 and cur2:
            cur3.next = ListNode(cur1.val + cur2.val)
            cur1, cur2, cur3 = cur1.next, cur2.next, cur3.next
        
        while cur1:
            cur3.next = ListNode(cur1.val)
            cur1, cur3 = cur1.next, cur3.next
            

        while cur2:
            cur3.next = ListNode(cur2.val)
            cur2, cur3 = cur2.next, cur3.next

        # Handle overflow
        cur = dummy.next
        while cur:
            if cur.val > 9:
                cur.val = cur.val % 10
                if cur.next:
                    cur.next.val += 1
                else:
                    cur.next = ListNode(1)
            cur = cur.next

        
        return dummy.next