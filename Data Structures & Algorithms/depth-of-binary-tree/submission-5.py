# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        def dfs(node, depth):
            if node is None:
                return depth
            
            # we increment depth to account for current node then make calls
            
            # get max of right depth and max of left depth, return max
            depth += 1
            right = dfs(node.right, depth)
            left = dfs(node.left, depth)
            return max(right, left)
            
        
        return dfs(root, 0)