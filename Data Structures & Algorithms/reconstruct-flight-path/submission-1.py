class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src : [] for src, dst in tickets}

        # sort tickets in lexical order
        tickets.sort() # sorts tickets based on pair by default

        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                # return true, valid path found
                return True
            
            if src not in adj:
                # src has no outgoing edges
                # return false b/c no valid path is found
                return False

            temp = list(adj[src]) # allows us to update actual adj list
            # enumerate allows us to iterate over index (i) and vertex (v)
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v): return True

                adj[src].insert(i, v)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res