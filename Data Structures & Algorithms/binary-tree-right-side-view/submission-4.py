# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs
        q = deque([root])
        res = []
        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node: # verify current node is not null
                    # this will always set rightSide to the right most node
                    # since it would be overwritten after each iteration
                    rightSide = node

                    # left before right
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)

        return res
