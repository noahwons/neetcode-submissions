# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        # First if does not execute, bot are not null, one might be
        # Hence second if. Include value check
        if not p or not q or p.val != q.val:
            return False
        
        # At this point, p and q are not empty and have the same value
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))