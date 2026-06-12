class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        visit = set()

        # Find rotten fruit
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visit.add((i, j))
        
        mins = 0
        while q:
            for _ in range(len(q)):
                curI, curJ = q.popleft()
                for di, dj in directions:
                    newI, newJ = curI + di, curJ + dj
                    if newI in range(rows) and newJ in range(cols) and grid[newI][newJ] == 1 and (newI, newJ) not in visit:
                        visit.add((newI, newJ))
                        grid[newI][newJ] = 2
                        q.append([newI, newJ])
            if len(q) > 0:
                mins += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return mins