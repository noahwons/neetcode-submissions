# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        # No arrays to traverse
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # root is always at the first index
        mid = inorder.index(preorder[0]) # gets the index of the root element from postorder
        
        # build left subtree recursively ==================================

        # Note: mid tells us how many nodes we want in left subtree
        # This, crete left subtree by creating the subarray from index 1
        # (skipping idx 0 since already accounted for) to mid + 1 since mid
        # is exclusive
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # pass new subarrays
        
        # build right subtree recursively ==================================

        # Note: to build right subtree, we need every value after this sublist: preorder[1:mid + 1]
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        # ==================================================================

        return root
