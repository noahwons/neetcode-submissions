# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def dfs(node):
            if not node:
                return
            
            heapq.heappush(heap, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(heap)
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        
        return heapq.heappop(heap)