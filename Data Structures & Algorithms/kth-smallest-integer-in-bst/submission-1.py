# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # idea: convert bst to heap, pop k times and return

        minHeap = []

        def dfs(node, minHeap):
            if node is None:
                return
            
            heapq.heappush(minHeap, node.val)

            dfs(node.right, minHeap)
            dfs(node.left, minHeap)
        
        dfs(root, minHeap)
        print(minHeap)

        while k > 1:
            heapq.heappop(minHeap)
            k -= 1
        
        return minHeap[0]