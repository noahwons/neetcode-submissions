# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we can run dfs on tree and return max val

        def dfs(node):
            if not node:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)

            return max(1 + right, 1 + left)
        
        return dfs(root)