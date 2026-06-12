class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            # none is graph
            return True

        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(prev, node):
            if node in visit:
                return False
            
            visit.add(node)
            
            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(node, j):
                    return False
            
            # no loop
            return True
        
        return dfs(-1, 0) and len(visit) == n