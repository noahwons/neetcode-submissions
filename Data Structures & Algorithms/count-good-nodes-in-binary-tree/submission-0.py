# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node is good if the path to it contains no value
        # greater than itself
        def dfs(curr, maxVal):
            if not curr:
                return 0

            if curr.val >= maxVal:
                return 1 + dfs(curr.left, curr.val) + dfs(curr.right, curr.val)
            
            return dfs(curr.left, maxVal) + dfs(curr.right, maxVal)
        
        return dfs(root, root.val)
            