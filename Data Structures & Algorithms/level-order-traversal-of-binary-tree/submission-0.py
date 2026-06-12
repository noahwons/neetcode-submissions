# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
    
        q = deque([root])
        while q:
            level = []

            # adds all elements in current level to level arr
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    # potentially adds null nodes, this is dealt with if level 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            # add all from current level to res
            if level:
                res.append(level)   
            

        return res

