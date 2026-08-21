# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if node.left is None and node.right is None:
                res = max(res, node.val)
            
            maxLeft, maxRight = float('-inf'), float('-inf')
            if node.left is not None:
                maxLeft = dfs(node.left)
            if node.right is not None:
                maxRight = dfs(node.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)
            res = max(res, (maxLeft + maxRight + node.val))
            return max((node.val + maxLeft), (node.val + maxRight))
        dfs(root)
        return res
        