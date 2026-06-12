class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        maxSize = 0

        if not grid:
            return 0
        
        def bfs(r, c):
            size = 1
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == 1 and 
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        size += 1

            return size
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxSize = max(maxSize, bfs(r, c))
        
        return maxSize
            