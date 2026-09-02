# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preform level order traversal of the tree
        # we build the result string as we go with N representing Null
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        self.i = 0
        print(arr)
        # left is at i + 1
        # right is at i + 2
        root = TreeNode(arr[0])
        def dfs():
            if arr[self.i] == 'N':
                # we can increament since we have null
                self.i += 1
                return None
            
            node = TreeNode(int(arr[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

