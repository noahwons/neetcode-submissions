class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)] # for every node i, its parent should be itself
        rank = [1] * (N + 1)

        def find(n):
            if n == par[n]:
                return par[n]
            
            par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            # preform union by rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            # return true if not connected
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]