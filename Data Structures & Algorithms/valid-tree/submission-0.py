class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            # empty graph is a tree
            return True

        adjList = {i : [] for i in range(n)}

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        seen = set()

        def dfs(prev, node):
            if node in seen:
                # invalid:
                return False
                
            seen.add(node)

            for child in adjList[node]:
                if child == prev:
                    continue
                if not dfs(node, child): 
                    return False
            # a loop was not detected
            return True
        
        # pass -1 as the prev value because it will never exist
        # remember the len of seen must be equal to n otherwise
        # there are nodes not attached to the graph
        return dfs(-1, 0) and len(seen) == n