# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 
        # if p.val and q.val greater than root, we know to traverse right
        # else if p.val and q.val are less than the root, we know to traverse left
        # else if p is greater than root and q is less than the root, we know we have a split
        # therefore we reutrn the root
        # edge case where one of the nodes is equal to the root. in this case, this node must
        # be the LCA
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        
        return root
        
