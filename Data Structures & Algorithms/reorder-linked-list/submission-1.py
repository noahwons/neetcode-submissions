# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []

        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        l, r = 0, len(arr) - 1
        while l < r:
            tmp = arr[l].next
            arr[l].next = arr[r]
            arr[r].next = tmp
            l += 1
            r -= 1
        if arr:
            arr[l].next = None

