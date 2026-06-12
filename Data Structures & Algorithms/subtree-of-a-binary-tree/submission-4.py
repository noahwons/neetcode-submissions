# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse via dfs, if root nodes are equal, verify that structure is valid
        if not root:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
                
            
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    
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
    