# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # let n represent the number of elements we have visited
        # once n = k, we have visited the value we are looking for
        # and can thus return that value
        n = 0
        stack = [] # required for iterative solution
        cur = root

        while cur or stack:
            while cur:
                # keep going left
                # visit every node in the left sub tree

                # NOTE: Since we have to visit cur AFTEr
                # the left node in an in order traversal,
                # we must append it to the stack so that
                # we have access to it and it can then be
                # processed.
                stack.append(cur) # put cur in stack so 

                cur = cur.left # move left

            # went to far, cur is at null
            cur = stack.pop() # collet most recently added value

            # process cur
            n += 1
            # we are gauranteed at least k elements, so we dont 
            # need an outside return satement
            if n == k:
                # cur node is the value we are looking for
                return cur.val
            
            # now visit right sub tree
            cur = cur.right
