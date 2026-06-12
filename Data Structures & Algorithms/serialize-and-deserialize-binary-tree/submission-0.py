# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] # store values, join at end with comma delimeter

        def dfs(node):
            if not node:
                res.append("N") # Let N represent null
                return
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0 # global so we can access in dfs function
        
        def dfs():
            # base case if pointer pointing to null
            if vals[self.i] == "N":
                self.i += 1 # increment so that next time we call function we are at appropriate value
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()





