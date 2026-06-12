class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        # create adjacency list
        for u, v, w in times:
            edges[u].append((v, w))

        # create minheap, init with first val and 0 b/c costs 0 time to visit source
        minHeap = [(0, k)]
        visit = set()
        t = 0 # store result
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2)) # add w1 + w2 so we have entire time

        return t if len(visit) == n else -1
        # Time: O(E * logV)
        

        