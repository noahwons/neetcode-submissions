# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse via dfs, if root nodes are equal, verify that structure is valid
        if not subRoot:
            # Null must always be a subtree of root
            return True
        if not root:
            # if we reach this case, subroot exists and root does not
            # since the subroot cannot be a subroot of nothing, we 
            # return false
            return False

        # We want to make it so that we check if they are the same 
        # But we should not immedietly return the result of isSameTree
        # Because we may have duplicate elements appearing in the tree
        # For the case root = [1, 1] and subroot = [1], if we directly call
        # is same tree while looking at the first 1, we would return false
        # since root has a left child and subroot does not. Thus, we should
        # have it so that the opportunity still exists
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
                
            
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        # compare values
        if p and q and p.val == q.val:
            # compare rest of trees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # Return false here because in this case, one tree is empty and one is not,
        # therefore they are not the same
        return False
