# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return
        
        heap = []

        for i, l in enumerate(lists):
            heapq.heappush(heap, (l.val, i, l))
        
        res = ListNode()
        tmp = res
        while heap:
            cur = heapq.heappop(heap)
            tmp.next = ListNode(cur[0])
            tmp = tmp.next
            if cur[2].next:
                heapq.heappush(heap, (cur[2].next.val, cur[1], cur[2].next))
        
        return res.next

        

            
        

