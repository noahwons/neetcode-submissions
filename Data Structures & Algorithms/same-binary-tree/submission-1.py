# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            # empty trees are equal
            return True
        
        if not p or not q:
            # one is null, one is not:
            return False
        
        if p.val != q.val:
            return False

        # both nodes p and q are non empty and same

        # recursive step
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

            