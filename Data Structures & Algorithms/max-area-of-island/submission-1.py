class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxSize = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            size = 1
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r, c) not in visit and r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        q.append((r, c))
                        visit.add((r, c))
                        size += 1

            return size

        for r in range(rows):
            for c in range(cols):
                # target value + not visited
                if grid[r][c] == 1 and (r, c) not in visit:
                    # run bfs
                    maxSize = max(maxSize, bfs(r, c))
        
        return maxSize