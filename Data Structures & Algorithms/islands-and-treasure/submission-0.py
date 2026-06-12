class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # run bfs to determine how to move
        # use locations 
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # for each gate, change gate to cur dist
                # gates start with value of 0
                # after first pop, neighbors are added

                grid[r][c] = dist

                # add all 4 adjacent rooms to queue
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

        
