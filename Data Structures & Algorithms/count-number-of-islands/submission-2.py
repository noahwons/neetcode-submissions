class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visit = set()

        def bfs(i, j):
            q = collections.deque([(i, j)])
            visit.add((i, j))

            while q:
                curI, curJ = q.popleft()
                for di, dj in directions:
                    newI, newJ = curI + di, curJ + dj
                    if (newI, newJ) not in visit and newI in range(rows) and newJ in range(cols) and grid[newI][newJ] == "1" :
                        visit.add((newI, newJ))
                        q.append((newI, newJ))


        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    islands += 1
        
        return islands