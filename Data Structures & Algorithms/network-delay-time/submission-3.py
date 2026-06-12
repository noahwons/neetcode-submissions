class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        

        pq = [(0, k)]
        visit = set()
        res = 0
        while pq:
            cur_dist, cur_node = heapq.heappop(pq)

            if cur_node in visit:
                continue

            visit.add(cur_node)
            res = cur_dist

            for nei, w in graph[cur_node]:
                new_dist = w + cur_dist
                if nei not in visit:
                    heapq.heappush(pq, (new_dist, nei))

        return res if len(visit) == n else -1