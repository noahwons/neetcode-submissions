# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal is bfs

        def bfs(root):
            q = collections.deque([root])
            res = []
            while q:
                level = []
                for i in range(len(q)):
                    # current q length is the num of elements in the current level
                    # so, we add each of these elements to our level array
                    cur = q.popleft()
                    if cur:
                        level.append(cur.val)
                        q.append(cur.left)
                        q.append(cur.right)
                # if we have a level array, we can add the level to the result
                if level:
                    res.append(level)
            return res
        
        return bfs(root)
                    
