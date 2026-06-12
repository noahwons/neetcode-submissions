# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxWidth = 0
        
        def dfs(node):
            if node == None:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)

            totalWidth = right + left
            self.maxWidth = max(self.maxWidth, totalWidth)

            return max(left, right) + 1
        
        dfs(root)
        return self.maxWidth