class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # We want to init a q with location of rotten fruit
        # then we run bfs and increment minute
        total_fruit = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    total_fruit += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        
        
        unique_fruit = 0
        time = 0
        while q:
            level_size = len(q)
            spread = False
            for _ in range(level_size):
                r, c = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visit and grid[nr][nc] == 1:
                        spread = True
                        q.append([nr, nc])
                        visit.add((nr, nc))
                        unique_fruit += 1

            if spread:
                # we have added at least one more child
                time += 1
            
        if unique_fruit < total_fruit:
            return -1
        return time

        