class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # idea, find treasure and run bfs from it, incrementing by layer
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        def addRoom(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or grid[r][c] == -1:
                # invalid
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            # inc dist after each layer
            dist += 1

                    
