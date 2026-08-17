# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()

        def dfs(node):
            if not node:
                return False
            
            if node not in visit:
                visit.add(node)
                res = dfs(node.next)
            
            else:
                return True
            
            return res
            
        return dfs(head)