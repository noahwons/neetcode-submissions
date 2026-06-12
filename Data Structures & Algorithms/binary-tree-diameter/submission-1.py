# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            
            # here, we want to get the width
            # or diameter of our current node
            # this is done by finding the width
            # of the left and right

            # In the smallest case, we have one parent
            # with two child nodes
            # Each child has a width of 0 (no children)
            # this each child would return 1 + max(0, 0)
            # we use max here to determine the max dist
            # we must travel to traverse that reigon
            L = dfs(node.right)
            R = dfs(node.left)

            # since any given node may have the greatest widht,
            # we update res each iteration (recursive call)
            self.res = max(self.res, (L + R))

            return 1 + max(L, R)
        
        dfs(root)
        
        return self.res



