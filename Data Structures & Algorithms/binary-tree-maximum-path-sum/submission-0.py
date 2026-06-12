# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # global result var
        res = [root.val]

        def dfs(root):
            # base case (dont have root)
            if not root:
                return 0

            # return max pathsum without splitting
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # avoid negative nums
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max pathsum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return value is what we compute WITHOUT splitting
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]