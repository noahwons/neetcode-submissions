# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        # ==================
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # ==================

        # Iterative BFS
        # ==================
        if not root:
            return 0
        
        level = 0
        q = deque([root]) # init w root element
        while q:
            # remove all elements currently in queue
            for i in range(len(q)):
                node = q.popleft()

                # then replace w children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level
            
        # ==================