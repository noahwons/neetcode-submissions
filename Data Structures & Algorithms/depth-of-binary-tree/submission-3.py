# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # find depth of binary tree

        # find max dfs traversal

        def dfs(node):
            if node == None:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)

            return max(right,left) + 1
        
        
        return dfs(root)