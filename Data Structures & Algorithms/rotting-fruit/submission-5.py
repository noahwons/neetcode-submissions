class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(n*m) time complexity (visiting each cell once)

        q = collections.deque()
        time, fresh = 0, 0

        ROWS = len(grid)
        COLS = len(grid[0])
        # iterate over grid
        for r in range(ROWS):
            for c in range(COLS):
                # keep track of all fresh fruit
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    # add all rotting to queue
                    q.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # if q or empty or fresh = 0, exit loop
        while q and fresh > 0:

            # pop all current fruit (clear queue) and add adjacent
            # Example: len(q) = 3, loop runs 3 times and adds all neighbors
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # ensure in bounds and non rotten (fresh) fruit. Then make rotten
                    if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != 1:
                        continue

                    # mark rotten (this prevents the need for a visit set)
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1
        