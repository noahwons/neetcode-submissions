class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit = set()
        maxArea = 0

        def bfs(i, j):
            q = collections.deque([(i, j)])
            visit.add((i, j))
            curArea = 1

            while q:
                curI, curJ = q.popleft()
                for di, dj in directions:
                    newI, newJ = curI + di, curJ + dj
                    if newI in range(rows) and newJ in range(cols) and grid[newI][newJ] == 1 and (newI, newJ) not in visit:
                        curArea += 1
                        q.append((newI, newJ))
                        visit.add((newI, newJ))
            
            return curArea
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    maxArea = max(maxArea, bfs(i, j))
        
        return maxArea
