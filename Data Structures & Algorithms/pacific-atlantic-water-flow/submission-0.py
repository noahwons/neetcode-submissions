class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(visit, r, c):
            # conditions for pacific: r == 0 or c == 0
            # conditions for atlantic r == len(heights) or c == len(heights[0])
            atlantic = False
            pacific = False
            q = collections.deque()
            q.append([r, c])
            visit.add((r, c))
            if r == 0 or c == 0:
                pacific = True
            if r == ROWS-1 or c == COLS-1:
                atlantic = True

            while q:
                r, c = q.popleft()

                
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and (row, col) not in visit and heights[row][col] <= heights[r][c]:
                        q.append([row, col])
                        visit.add((row, col))
                        if row == 0 or col == 0:
                            pacific = True
                        if row == ROWS-1 or col == COLS-1:
                            atlantic = True
        
            # after this runs, in order for it to be valid both pacific and atlantic must be true
            return atlantic and pacific
    
        for r in range(ROWS):
            for c in range(COLS):
                visit = set()
                if bfs(visit, r, c):
                    res.append([r, c])
        
        return res
