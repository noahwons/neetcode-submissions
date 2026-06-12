class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        adj = {i : [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(prev, node):    
            visit.add(node)
            
            # increment through neighbors, skip prev
            for n in adj[node]:
                if n == prev:
                    continue
                if n not in visit:
                    dfs(node, n)
            
            return 1
 
            
        total = 0
        for i in range(n):
            if i not in visit:
                total += dfs(-1, i)
        return total