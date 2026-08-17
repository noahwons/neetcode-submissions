# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        visit = set()
        while cur:
            if cur in visit:
                return True
            else:
                visit.add(cur)
                cur = cur.next
        return False