# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we can do backtracking dfs to explore every path and determine the max
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if node.left is None and node.right is None:
                res = max(res, node.val)
                return node.val

            # max at a position is the max(maxLeft, maxRight, (maxLeft + maxRight + node.val))
            # in order to update res we take the max of res we can split
            # res = max(res, (maxLeft + maxRight + node.val))
            # we return to parent, the max path without split
            # return max((node.val + maxLeft), (node.val + maxRight))

            maxLeft, maxRight = float('-inf'), float('-inf')
            if node.left is not None:
                maxLeft = dfs(node.left)

            if node.right is not None:
                maxRight = dfs(node.right)

            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            res = max(res, (maxLeft + maxRight + node.val))
            return max((node.val + maxLeft), (node.val + maxRight))
            
            
            # if our current value is positive, then we can add it to the path
            # this means we have (max(left) + max(right) + cur.val)

            # if our current value is negative, then we simply return the max
            # of left and right trees
        dfs(root)
        return res
        
        
